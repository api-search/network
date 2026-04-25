#!/usr/bin/env python3
"""
Bootstrap all subdomain Jekyll sites from the shared template.
Copies shared layouts, assets, and creates site-specific configs and index pages.
"""

import os
import shutil
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NETWORK_DIR = os.path.join(ROOT_DIR, 'network')
SHARED_DIR = os.path.join(NETWORK_DIR, '_shared')

# Site definitions: (repo_name, subdomain, site_name, nav_active, collection_name, collection_type, layout_source, description)
SITES = [
    {
        'repo': 'providers',
        'subdomain': 'providers.apis.io',
        'name': 'APIs.io Providers',
        'nav_active': 'providers',
        'collection': 'providers',
        'collection_type': 'providers',
        'layout': 'provider',
        'permalink': '/providers/:path/',
        'description': 'Browse API service providers across the APIs.io network.',
    },
    {
        'repo': 'apis',
        'subdomain': 'apis.apis.io',
        'name': 'APIs.io APIs',
        'nav_active': 'apis',
        'collection': 'apis',
        'collection_type': 'apis',
        'layout': 'api',
        'permalink': '/apis/:path/',
        'description': 'Browse individual APIs across the APIs.io network.',
    },
    {
        'repo': 'capabilities',
        'subdomain': 'capabilities.apis.io',
        'name': 'APIs.io Capabilities',
        'nav_active': 'capabilities',
        'collection': 'capabilities',
        'collection_type': 'capabilities',
        'layout': 'capability',
        'permalink': '/capabilities/:path/',
        'description': 'Browse API capabilities and workflows across the APIs.io network.',
    },
    {
        'repo': 'schemas',
        'subdomain': 'schemas.apis.io',
        'name': 'APIs.io Schemas',
        'nav_active': 'more',
        'collection': 'schemas',
        'collection_type': 'schemas',
        'layout': 'schema',
        'permalink': '/schemas/:path/',
        'description': 'Browse JSON Schema definitions across the APIs.io network.',
    },
    {
        'repo': 'asyncapi',
        'subdomain': 'asyncapi.apis.io',
        'name': 'APIs.io AsyncAPI',
        'nav_active': 'more',
        'collection': 'asyncapis',
        'collection_type': 'asyncapis',
        'layout': 'asyncapi',
        'permalink': '/asyncapis/:path/',
        'description': 'Browse AsyncAPI event specifications across the APIs.io network.',
    },
    {
        'repo': 'json-ld',
        'subdomain': 'json-ld.apis.io',
        'name': 'APIs.io JSON-LD',
        'nav_active': 'more',
        'collection': 'jsonld',
        'collection_type': 'jsonld',
        'layout': 'jsonld',
        'permalink': '/jsonld/:path/',
        'description': 'Browse JSON-LD semantic vocabularies across the APIs.io network.',
    },
    {
        'repo': 'rules',
        'subdomain': 'rules.apis.io',
        'name': 'APIs.io Rules',
        'nav_active': 'more',
        'collection': 'rules',
        'collection_type': 'rules',
        'layout': 'rules',
        'permalink': '/rules/:path/',
        'description': 'Browse API governance rules and Spectral rulesets across the APIs.io network.',
    },
    {
        'repo': 'tags',
        'subdomain': 'tags.apis.io',
        'name': 'APIs.io Tags',
        'nav_active': 'tags',
        'collection': None,  # No collection - aggregates from search indexes
        'collection_type': None,
        'layout': None,
        'permalink': None,
        'description': 'Browse APIs, capabilities, and more by tag across the APIs.io network.',
    },
    {
        'repo': 'vocabularies',
        'subdomain': 'vocabularies.apis.io',
        'name': 'APIs.io Vocabularies',
        'nav_active': 'more',
        'collection': None,  # Uses _data/vocabulary.json
        'collection_type': None,
        'layout': None,
        'permalink': None,
        'description': 'Advanced vocabulary search across resources, actions, personas, domains, and schemas.',
    },
    {
        'repo': 'examples',
        'subdomain': 'examples.apis.io',
        'name': 'APIs.io Examples',
        'nav_active': 'more',
        'collection': None,
        'collection_type': None,
        'layout': None,
        'permalink': None,
        'description': 'API usage examples across the APIs.io network.',
    },
]


def copy_shared(site_dir):
    """Copy shared layouts and assets to site."""
    # Layouts
    shared_layouts = os.path.join(SHARED_DIR, '_layouts')
    site_layouts = os.path.join(site_dir, '_layouts')
    os.makedirs(site_layouts, exist_ok=True)
    shutil.copy2(os.path.join(shared_layouts, 'default.html'), os.path.join(site_layouts, 'default.html'))

    # Assets
    shared_assets = os.path.join(SHARED_DIR, 'assets')
    site_assets = os.path.join(site_dir, 'assets')
    if os.path.exists(site_assets):
        shutil.rmtree(site_assets)
    shutil.copytree(shared_assets, site_assets)


def write_config(site_dir, site):
    """Write _config.yml for the site."""
    lines = [
        f"name: {site['name']}",
        f"description: {site['description']}",
        "image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg",
        f"url: https://{site['subdomain']}",
        "",
        "node: website",
        f"nav_active: {site['nav_active']}",
        "",
        "keywords:",
        "  - APIs",
        "  - Search",
        "  - Discovery",
        "",
        'exclude: [".rvmrc", ".rbenv-version", "README.md", "Rakefile", "changelog.md", "scripts"]',
        'include: [".well-known"]',
        "",
        "github_org: api-search",
        f"github_repo: {site['repo']}",
        "",
    ]

    if site['collection']:
        lines.extend([
            "collections:",
            f"  {site['collection']}:",
            "    output: true",
            f"    permalink: {site['permalink']}",
            "",
            "defaults:",
            "  - scope:",
            '      path: ""',
            f"      type: {site['collection_type']}",
            "    values:",
            f"      layout: {site['layout']}",
            "",
        ])

    config_path = os.path.join(site_dir, '_config.yml')
    with open(config_path, 'w') as f:
        f.write('\n'.join(lines))


def write_gemfile(site_dir):
    """Write Gemfile."""
    with open(os.path.join(site_dir, 'Gemfile'), 'w') as f:
        f.write("source 'https://rubygems.org'\ngem 'github-pages', group: :jekyll_plugins\n")


def write_gitignore(site_dir):
    """Write .gitignore."""
    with open(os.path.join(site_dir, '.gitignore'), 'w') as f:
        f.write("_site/\n.jekyll-cache/\n.jekyll-metadata\n.sass-cache/\nGemfile.lock\n")


def write_cname(site_dir, subdomain):
    """Write CNAME for GitHub Pages."""
    with open(os.path.join(site_dir, 'CNAME'), 'w') as f:
        f.write(subdomain + '\n')


ROBOTS_TEMPLATE = """---
layout: none
---
# NOTICE: APIs.io is a public catalog of API metadata intended for both human
# and machine consumption. Indexing, AI inference (RAG/grounding), and training
# are all explicitly permitted. See https://apis.io/terms/ for the terms of use.

User-agent: *
Allow: /

# Cloudflare Content Signals (https://blog.cloudflare.com/content-signals-policy/)
Content-Signal: search=yes, ai-input=yes, ai-train=yes

# AIPREF Content-Usage (draft-ietf-aipref-attach)
Content-Usage: search=y, ai-input=y, ai-train=y

Sitemap: {{ site.url }}/sitemap.xml
"""


def write_robots(site_dir):
    """Write robots.txt with Cloudflare Content Signals + AIPREF Content-Usage."""
    with open(os.path.join(site_dir, 'robots.txt'), 'w') as f:
        f.write(ROBOTS_TEMPLATE)


def sitemap_template(collection):
    """Return a Jekyll sitemap.xml template scoped to one collection (or none)."""
    head = """---
layout: none
---
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{{ site.url }}/</loc>
    <priority>1.0</priority>
  </url>
"""
    body = ""
    if collection:
        body = (
            "  {% for item in site." + collection + " %}\n"
            "  <url>\n"
            "    <loc>{{ site.url }}{{ item.url }}</loc>\n"
            "    <priority>0.7</priority>\n"
            "  </url>\n"
            "  {% endfor %}\n"
        )
    tail = "</urlset>\n"
    return head + body + tail


def write_sitemap(site_dir, collection):
    """Write a Jekyll sitemap.xml scoped to the site's collection."""
    with open(os.path.join(site_dir, 'sitemap.xml'), 'w') as f:
        f.write(sitemap_template(collection))


def copy_type_layout(site_dir, layout_name):
    """Copy type-specific layout from network."""
    src = os.path.join(NETWORK_DIR, '_layouts', f'{layout_name}.html')
    dst = os.path.join(site_dir, '_layouts', f'{layout_name}.html')
    if os.path.exists(src):
        shutil.copy2(src, dst)


def main():
    print("=== Bootstrapping Subdomain Sites ===")

    for site in SITES:
        site_dir = os.path.join(ROOT_DIR, site['repo'])
        print(f"\n--- {site['repo']} ({site['subdomain']}) ---")

        if not os.path.isdir(site_dir):
            print(f"  WARNING: {site_dir} does not exist, skipping")
            continue

        # Copy shared assets and layouts
        copy_shared(site_dir)
        print("  Copied shared layout and assets")

        # Copy type-specific layout
        if site['layout']:
            copy_type_layout(site_dir, site['layout'])
            print(f"  Copied {site['layout']}.html layout")

        # Write config
        write_config(site_dir, site)
        print("  Wrote _config.yml")

        # Write Gemfile
        write_gemfile(site_dir)
        print("  Wrote Gemfile")

        # Write .gitignore
        write_gitignore(site_dir)
        print("  Wrote .gitignore")

        # Write CNAME
        write_cname(site_dir, site['subdomain'])
        print(f"  Wrote CNAME: {site['subdomain']}")

        # Write robots.txt + sitemap.xml
        write_robots(site_dir)
        write_sitemap(site_dir, site['collection'])
        print("  Wrote robots.txt and sitemap.xml")

        # Create collection directory if needed
        if site['collection']:
            coll_dir = os.path.join(site_dir, f"_{site['collection']}")
            os.makedirs(coll_dir, exist_ok=True)
            print(f"  Created _{site['collection']}/ directory")

    print("\n=== Bootstrap Complete ===")


if __name__ == '__main__':
    main()
