#!/usr/bin/env python3
"""
Generate provider icons using Google Gemini Imagen API.

Reads provider data from _providers/ markdown files, identifies which
providers need icons (missing or using placeholder), generates icons
via Gemini, saves them to assets/icons/, and updates the provider
front matter to use the new local icon path.

Tracks generated icons in assets/icons/manifest.json to avoid
regenerating existing ones.
"""

import os
import sys
import json
import glob
import time
import yaml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
NETWORK_DIR = os.path.dirname(SCRIPT_DIR)
PROVIDERS_DIR = os.path.join(NETWORK_DIR, '_providers')
ICONS_DIR = os.path.join(NETWORK_DIR, 'assets', 'icons')
MANIFEST_PATH = os.path.join(ICONS_DIR, 'manifest.json')

PLACEHOLDER_PATTERNS = ['apis-json-logo', 'example.com']


def load_manifest():
    if os.path.exists(MANIFEST_PATH):
        with open(MANIFEST_PATH) as f:
            return json.load(f)
    return {}


def save_manifest(manifest):
    os.makedirs(ICONS_DIR, exist_ok=True)
    with open(MANIFEST_PATH, 'w') as f:
        json.dump(manifest, f, indent=2, sort_keys=True)


def get_providers_needing_icons():
    """Return list of (slug, name) for providers without proper icons."""
    manifest = load_manifest()
    needs = []

    for f in sorted(glob.glob(os.path.join(PROVIDERS_DIR, '*.md'))):
        with open(f) as fh:
            content = fh.read()
        parts = content.split('---')
        if len(parts) < 3:
            continue
        data = yaml.safe_load(parts[1])
        slug = data.get('slug', os.path.basename(f).replace('.md', ''))
        name = data.get('name', slug)
        image = data.get('image', '')

        # Already generated
        if slug in manifest:
            continue

        # Has a real image
        if image and not any(p in image for p in PLACEHOLDER_PATTERNS) and image != '':
            continue

        needs.append((slug, name))

    return needs


def generate_icon(name, slug, api_key):
    """Generate an icon for a provider using Gemini Imagen."""
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)

    prompt = (
        f"A clean, modern, minimalist icon representing {name} as a technology company or software platform. "
        f"Simple flat design, single iconic symbol, vibrant colors on a clean white background. "
        f"Professional corporate style suitable for a small icon. No text, no words, no letters."
    )

    try:
        response = client.models.generate_images(
            model='imagen-4.0-generate-001',
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
            )
        )

        if response.generated_images:
            img_bytes = response.generated_images[0].image.image_bytes
            icon_path = os.path.join(ICONS_DIR, f"{slug}.png")
            with open(icon_path, 'wb') as f:
                f.write(img_bytes)
            return True
        else:
            print(f"  WARNING: No image generated for {name}")
            return False
    except Exception as e:
        print(f"  ERROR generating icon for {name}: {e}")
        return False


def update_provider_image(slug):
    """Update the provider markdown file to use the generated icon."""
    provider_path = os.path.join(PROVIDERS_DIR, f"{slug}.md")
    if not os.path.exists(provider_path):
        return

    with open(provider_path) as f:
        content = f.read()

    parts = content.split('---')
    if len(parts) < 3:
        return

    data = yaml.safe_load(parts[1])
    data['image'] = f"/assets/icons/{slug}.png"

    with open(provider_path, 'w') as f:
        f.write('---\n')
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, width=1000)
        f.write('---\n')
        if len(parts) > 2:
            f.write(parts[2])


def main():
    # Load API key
    env_path = os.path.join(os.path.dirname(NETWORK_DIR), '.env')
    api_key = None
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if line.startswith('GEMINI_KEY='):
                    api_key = line.strip().split('=', 1)[1]
                    break

    if not api_key:
        print("ERROR: GEMINI_KEY not found in .env")
        sys.exit(1)

    os.makedirs(ICONS_DIR, exist_ok=True)
    manifest = load_manifest()
    needs = get_providers_needing_icons()

    if not needs:
        print("All providers have icons. Nothing to generate.")
        return

    print(f"=== Icon Generation ===")
    print(f"Need to generate: {len(needs)} icons")
    print()

    generated = 0
    failed = 0

    for slug, name in needs:
        print(f"  Generating: {name} ({slug})...")
        if generate_icon(name, slug, api_key):
            manifest[slug] = {
                'name': name,
                'file': f"{slug}.png",
                'generated': time.strftime('%Y-%m-%d'),
            }
            save_manifest(manifest)
            update_provider_image(slug)
            generated += 1
            print(f"    OK")
        else:
            failed += 1

        # Rate limit: ~10 requests per minute for Imagen
        time.sleep(6)

    print(f"\n=== Complete ===")
    print(f"Generated: {generated}")
    print(f"Failed:    {failed}")
    print(f"Total in manifest: {len(manifest)}")


if __name__ == '__main__':
    main()
