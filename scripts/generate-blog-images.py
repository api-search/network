#!/usr/bin/env python3
"""
Generate black and white blog post images using Google Gemini Imagen API.
"""

import os
import sys
import time
import yaml
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
NETWORK_DIR = os.path.dirname(SCRIPT_DIR)
POSTS_DIR = os.path.join(NETWORK_DIR, '_posts')
IMAGES_DIR = os.path.join(NETWORK_DIR, 'assets', 'images', 'blog')

# Load API key from .env
def load_api_key():
    env_path = os.path.join(os.path.dirname(NETWORK_DIR), '.env')
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if line.startswith('GEMINI_KEY='):
                    return line.strip().split('=', 1)[1]
    return os.environ.get('GEMINI_KEY')


def get_posts():
    """Get all posts with their titles and tags."""
    posts = []
    for f in sorted(glob.glob(os.path.join(POSTS_DIR, '*.md'))):
        with open(f) as fh:
            content = fh.read()
        parts = content.split('---')
        if len(parts) < 3:
            continue
        data = yaml.safe_load(parts[1])
        slug = os.path.basename(f).replace('.md', '')
        # Remove date prefix for image filename
        image_slug = slug[11:] if len(slug) > 11 else slug
        posts.append({
            'file': f,
            'slug': slug,
            'image_slug': image_slug,
            'title': data.get('title', ''),
            'tags': data.get('tags', []),
            'image': data.get('image', ''),
        })
    return posts


def generate_image(title, tags, image_slug, api_key):
    """Generate a black and white blog image."""
    from google import genai
    from google.genai import types

    tag_str = ', '.join(tags[:4]) if tags else 'API, technology'

    prompt = (
        f"A striking black and white editorial illustration for a blog post titled '{title}'. "
        f"Themes: {tag_str}. "
        f"Abstract, minimalist composition with clean geometric shapes and high contrast. "
        f"Think ink illustration style - bold blacks, crisp whites, no gray midtones. "
        f"Conceptual and evocative, suitable as a wide banner image. "
        f"No text, no words, no letters, no logos."
    )

    client = genai.Client(api_key=api_key)

    try:
        response = client.models.generate_images(
            model='imagen-4.0-generate-001',
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio='16:9',
            )
        )

        if response.generated_images:
            os.makedirs(IMAGES_DIR, exist_ok=True)
            img_path = os.path.join(IMAGES_DIR, f"{image_slug}.png")
            with open(img_path, 'wb') as f:
                f.write(response.generated_images[0].image.image_bytes)
            print(f"  Generated: {image_slug}.png")
            return True
        else:
            print(f"  No image generated for: {title}")
            return False
    except Exception as e:
        print(f"  ERROR generating image for {title}: {e}")
        return False


def update_post_image(filepath, new_image_path):
    """Update the image field in a blog post's front matter.

    Splits on the front-matter delimiters only (start and the matching
    closing `\\n---\\n`). A naive content.split('---') would also split
    on markdown table row separators in the body (e.g. `|---|---|`),
    truncating the post.
    """
    with open(filepath) as f:
        content = f.read()

    if not content.startswith('---\n'):
        return
    end = content.find('\n---\n', 4)
    if end == -1:
        return

    fm_text = content[4:end]
    body = content[end + 5:]

    data = yaml.safe_load(fm_text)
    data['image'] = new_image_path

    with open(filepath, 'w') as f:
        f.write('---\n')
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, width=1000)
        f.write('---\n')
        f.write(body)


def main():
    api_key = load_api_key()
    if not api_key:
        print("ERROR: No GEMINI_KEY found in .env or environment")
        sys.exit(1)

    posts = get_posts()
    print(f"Found {len(posts)} blog posts")

    for post in posts:
        image_path = os.path.join(IMAGES_DIR, f"{post['image_slug']}.png")

        # Skip if already generated
        if os.path.exists(image_path):
            print(f"  Skipping (exists): {post['image_slug']}")
            continue

        print(f"  Generating image for: {post['title']}")
        success = generate_image(post['title'], post['tags'], post['image_slug'], api_key)

        if success:
            new_image = f"/assets/images/blog/{post['image_slug']}.png"
            update_post_image(post['file'], new_image)
            print(f"  Updated front matter: {post['slug']}")

        # Rate limit
        time.sleep(6)

    print("\nDone!")


if __name__ == '__main__':
    main()
