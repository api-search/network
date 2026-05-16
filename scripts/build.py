#!/usr/bin/env python3
"""
Build script that reads api-evangelist repos and generates Jekyll collections
for the apis.io network of subdomain sites.

Outputs to separate repos:
  - providers/   -> providers.apis.io
  - apis/        -> apis.apis.io
  - capabilities/ -> capabilities.apis.io
  - schemas/     -> schemas.apis.io
  - asyncapi/    -> asyncapi.apis.io
  - json-ld/     -> json-ld.apis.io
  - rules/       -> rules.apis.io
  - vocabularies/ -> vocabularies.apis.io (vocabulary.json)
  - network/     -> apis.io (icon manifest stays here)
"""

import os
import sys
import json
import glob
import shutil
import re
import yaml


# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
NETWORK_DIR = os.path.dirname(SCRIPT_DIR)
ROOT_DIR = os.path.dirname(NETWORK_DIR)
EVANGELIST_DIR = os.environ.get('EVANGELIST_DIR') or os.path.join(ROOT_DIR, 'api-evangelist')
SHARED_DIR = os.path.join(NETWORK_DIR, '_shared')

# Output dirs - each goes to its own subdomain repo
PROVIDERS_DIR = os.path.join(ROOT_DIR, 'providers', '_providers')
APIS_DIR = os.path.join(ROOT_DIR, 'apis', '_apis')
CAPABILITIES_DIR = os.path.join(ROOT_DIR, 'capabilities', '_capabilities')
CATEGORIES_DIR = os.path.join(ROOT_DIR, 'capabilities', '_categories')
SCHEMAS_DIR = os.path.join(ROOT_DIR, 'schemas', '_schemas')
ASYNCAPIS_DIR = os.path.join(ROOT_DIR, 'asyncapi', '_asyncapis')
JSONLD_DIR = os.path.join(ROOT_DIR, 'json-ld', '_jsonld')
RULES_DIR = os.path.join(ROOT_DIR, 'rules', '_rules')
PLANS_DIR = os.path.join(ROOT_DIR, 'plans', '_plans')
RATELIMITS_DIR = os.path.join(ROOT_DIR, 'rate-limits', '_ratelimits')
FINOPS_DIR = os.path.join(ROOT_DIR, 'finops', '_finops')

# Canonical capability taxonomy + suggestions for the category aggregation layer.
CANONICAL_CAPS_PATH = os.path.join(NETWORK_DIR, '_data', 'canonical-capabilities.yml')
CATEGORY_SUGGESTIONS_PATH = os.path.join(NETWORK_DIR, '_data', 'category-suggestions.yml')
MIN_FALLBACK_SUGGESTION_SCORE = 5

# Inline source-widget content cap. Embeds over this size show a truncation
# notice plus the source URL — keeps the schemas repo from ballooning when a
# few specs (Salesforce metadata, etc.) are multi-megabyte.
SOURCE_WIDGET_MAX_BYTES = 32 * 1024

# Tags that are stripped from all output regardless of what the source repos say.
# Add entries here to suppress noise tags globally across every build.
TAG_BLOCKLIST = {'AWS'}


def filter_tags(tags):
    """Remove blocked tags from a tag list."""
    if not tags:
        return tags
    return [t for t in tags if t not in TAG_BLOCKLIST]


def cap_source(text, source_url):
    """Truncate inline source for the widget when oversized; keep the link."""
    if not text:
        return text
    raw = text.encode('utf-8', errors='replace')
    if len(raw) <= SOURCE_WIDGET_MAX_BYTES:
        return text
    head = raw[:SOURCE_WIDGET_MAX_BYTES].decode('utf-8', errors='replace')
    notice = (
        f"\n\n# --- truncated at {SOURCE_WIDGET_MAX_BYTES // 1024} KB "
        f"({len(raw) // 1024} KB total) ---\n"
        f"# Full source: {source_url}\n"
    )
    return head + notice

# Subdomain URLs for cross-linking
SUBDOMAINS = {
    'network': 'https://apis.io',
    'providers': 'https://providers.apis.io',
    'apis': 'https://apis.apis.io',
    'capabilities': 'https://capabilities.apis.io',
    'schemas': 'https://schemas.apis.io',
    'asyncapi': 'https://asyncapi.apis.io',
    'json-ld': 'https://json-ld.apis.io',
    'rules': 'https://rules.apis.io',
    'vocabularies': 'https://vocabularies.apis.io',
    'plans': 'https://plans.apis.io',
    'rate-limits': 'https://rate-limits.apis.io',
    'finops': 'https://finops.apis.io',
}


def slugify(text):
    """Convert text to URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def clean_description(desc):
    """Clean description for YAML front matter."""
    if not desc:
        return ''
    desc = str(desc).strip()
    desc = re.sub(r'\s+', ' ', desc)
    return desc


def write_frontmatter_file(filepath, data, body=''):
    """Write a Jekyll markdown file with YAML front matter."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write('---\n')
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, width=1000)
        f.write('---\n')
        if body:
            f.write(body)


def load_yaml(filepath):
    """Load a YAML file."""
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


def load_json(filepath):
    """Load a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def extract_api_slug(aid):
    """Extract slug from aid like 'google-analytics:google-analytics-data-api'."""
    if ':' in aid:
        return aid.split(':', 1)[1]
    return aid


def _derive_plans_meta(data):
    """Pull plans-specific metadata into the front matter."""
    plans = data.get('plans', []) if isinstance(data.get('plans'), list) else []
    return {
        'plan_count': len(plans),
        'plans': plans,
        'specification': data.get('specification', ''),
        'sources': data.get('sources', []),
    }


def _derive_ratelimits_meta(data):
    """Pull rate-limit-specific metadata into the front matter."""
    limits = data.get('limits', []) if isinstance(data.get('limits'), list) else []
    return {
        'limit_count': len(limits),
        'limits': limits,
        'policies': data.get('policies', []),
        'response_codes': data.get('responseCodes', {}) or {},
        'specification': data.get('specification', ''),
        'sources': data.get('sources', []),
    }


def _derive_finops_meta(data):
    """Pull FinOps-specific metadata into the front matter."""
    fc = data.get('focusColumns', {}) or {}
    return {
        'service_category': data.get('serviceCategory', ''),
        'publisher_name': data.get('publisherName', ''),
        'aligned_with': data.get('alignedWith', {}) or {},
        'billing_model': data.get('billingModel', {}) or {},
        'focus_columns': fc,
        'meters': data.get('meters', []),
        'specification': data.get('specification', ''),
        'sources': data.get('sources', []),
    }


def _process_provider_subdir(provider_dir, provider_slug, provider_name,
                             provider_data, provider_api_specs, github_raw_base,
                             subdir, out_dir, layout, source_heading, derive_meta):
    """Generic processor for plans/, rate-limits/, finops/ provider subdirs.

    Reads YAML files from <provider_dir>/<subdir>/, derives layout-specific
    metadata via derive_meta(yaml_data), and writes one Markdown file per
    source YAML to out_dir/<provider_slug>/<slug>.md.
    """
    src_dir = os.path.join(provider_dir, subdir)
    if not os.path.isdir(src_dir):
        return []

    files = sorted(glob.glob(os.path.join(src_dir, '*.yml')) +
                   glob.glob(os.path.join(src_dir, '*.yaml')))
    entries = []
    provider_tags = filter_tags(provider_data.get('tags', []) or [])

    for src_file in files:
        filename = os.path.basename(src_file)
        slug = os.path.splitext(filename)[0]
        try:
            data = load_yaml(src_file)
        except Exception:
            continue
        if not isinstance(data, dict):
            continue

        title = slug.replace('-', ' ').title()
        entry = {
            'layout': layout,
            'slug': slug,
            'name': title,
            'description': data.get('description', '') or '',
            'provider_name': provider_name,
            'provider_slug': provider_slug,
            'tags': filter_tags(data.get('tags', []) or []) or provider_tags,
            'source_filename': filename,
            'source_heading': source_heading,
        }
        # Layout-specific fields
        entry.update(derive_meta(data))

        # Cap embedded source for the YAML widget
        source_url = f"{github_raw_base}/{subdir}/{filename}"
        try:
            with open(src_file) as fh:
                entry['source_yaml'] = cap_source(fh.read(), source_url)
        except OSError:
            entry['source_yaml'] = ''
        entry['source_yaml_url'] = source_url
        entry['source_url'] = data.get('sources', [None])[0] if data.get('sources') else ''

        if provider_api_specs:
            entry['api_specs'] = provider_api_specs

        out_file = os.path.join(out_dir, provider_slug, f"{slug}.md")
        write_frontmatter_file(out_file, entry)
        entries.append(entry)

    return entries


def extract_schema_slug(filename):
    """Extract slug from schema filename."""
    slug = os.path.splitext(filename)[0]
    if slug.endswith('-schema'):
        slug = slug[:-7]
    return slug


def extract_capability_search_terms(cap_data, vocab_data, provider_tags):
    """Extract search terms from capability data for capability-first search."""
    terms = set()

    info = cap_data.get('info', {})
    for tag in info.get('tags', []):
        terms.add(tag.lower())

    capability = cap_data.get('capability', {})
    for exposed in capability.get('exposes', []):
        for resource in exposed.get('resources', []):
            desc = resource.get('description', '')
            if desc:
                terms.add(desc.lower())
            for op in resource.get('operations', []):
                name = op.get('name', '').replace('-', ' ')
                if name:
                    terms.add(name)
                op_desc = op.get('description', '')
                if op_desc:
                    terms.add(op_desc.lower())

        for tool in exposed.get('tools', []):
            tool_desc = tool.get('description', '')
            if tool_desc:
                terms.add(tool_desc.lower())
            tool_name = tool.get('name', '').replace('-', ' ')
            if tool_name:
                terms.add(tool_name)

    if vocab_data:
        cap_section = vocab_data.get('capability', {})
        if isinstance(cap_section, dict):
            for workflow in cap_section.get('workflows', []):
                if not isinstance(workflow, dict):
                    continue
                wf_desc = workflow.get('description', '')
                if wf_desc:
                    terms.add(wf_desc.lower())
                for persona_id in workflow.get('personas', []):
                    if isinstance(persona_id, str):
                        terms.add(persona_id.replace('-', ' '))

            for persona in cap_section.get('personas', []):
                if isinstance(persona, dict):
                    p_desc = persona.get('description', '')
                    if p_desc:
                        terms.add(p_desc.lower())
                elif isinstance(persona, str):
                    terms.add(persona.lower())

            for domain in cap_section.get('domains', []):
                if isinstance(domain, dict):
                    d_desc = domain.get('description', '')
                    if d_desc:
                        terms.add(d_desc.lower())
                elif isinstance(domain, str):
                    terms.add(domain.lower())

    for tag in provider_tags:
        terms.add(tag.lower())

    cleaned = []
    for term in terms:
        term = term.strip()
        if term and len(term) > 1:
            cleaned.append(term)
    return cleaned


def extract_operations_from_capability(cap_data):
    """Extract flattened operation list from capability exposes."""
    operations = []
    tools = []

    capability = cap_data.get('capability', {})
    for exposed in capability.get('exposes', []):
        expose_type = exposed.get('type', '')

        if expose_type == 'mcp':
            for tool in exposed.get('tools', []):
                tools.append({
                    'name': tool.get('name', ''),
                    'description': clean_description(tool.get('description', '')),
                    'hints': tool.get('hints', {})
                })
        else:
            for resource in exposed.get('resources', []):
                for op in resource.get('operations', []):
                    operations.append({
                        'name': op.get('name', ''),
                        'method': op.get('method', ''),
                        'description': clean_description(op.get('description', '')),
                        'path': resource.get('path', '')
                    })

    return operations, tools


def find_matching_workflow(cap_label, vocab_data):
    """Find the vocabulary workflow matching a capability label."""
    if not vocab_data:
        return None
    cap_section = vocab_data.get('capability', {})
    if not isinstance(cap_section, dict):
        return None
    for workflow in cap_section.get('workflows', []):
        if not isinstance(workflow, dict):
            continue
        if workflow.get('name', '').lower() == cap_label.lower():
            return workflow
        if workflow.get('name', '').lower() in cap_label.lower():
            return workflow
    return None


def process_provider(provider_dir, icon_manifest=None, category_suggestions=None, category_implementations=None):
    """Process a single api-evangelist provider repo."""
    apis_yml_path = os.path.join(provider_dir, 'apis.yml')
    if not os.path.exists(apis_yml_path):
        print(f"  Skipping {provider_dir} - no apis.yml")
        return None

    data = load_yaml(apis_yml_path)
    provider_slug = data.get('aid', os.path.basename(provider_dir))
    provider_name = data.get('name', provider_slug)
    provider_tags = filter_tags(data.get('tags', []))

    print(f"  Processing: {provider_name} ({provider_slug})")

    # Load vocabulary if available
    vocab_data = None
    vocab_files = glob.glob(os.path.join(provider_dir, 'vocabulary', '*-vocabulary.yaml'))
    if vocab_files:
        vocab_data = load_yaml(vocab_files[0])

    # --- Provider ---
    apis_list = data.get('apis', [])
    if not apis_list:
        print(f"  Skipping {provider_name} - no APIs")
        return None
    common = data.get('common', [])

    features = []
    use_cases = []
    integrations = []
    solutions = []
    skills = []
    common_resources = []

    for item in common:
        item_type = item.get('type', '')
        if item_type == 'Features':
            features = item.get('data', [])
        elif item_type == 'UseCases':
            use_cases = item.get('data', [])
        elif item_type == 'Integrations':
            integrations = item.get('data', [])
        elif item_type == 'Solutions':
            solutions = item.get('data', [])
        elif item_type == 'Skills':
            skills = item.get('data', [])
        else:
            common_resources.append({
                'type': item_type,
                'url': item.get('url', ''),
                'title': item.get('title', '')
            })

    provider_data = {
        'layout': 'provider',
        'slug': provider_slug,
        'name': provider_name,
        'description': clean_description(data.get('description', '')),
        'image': data.get('image', ''),
        'url': data.get('url', ''),
        'tags': provider_tags,
        'created': data.get('created', ''),
        'modified': data.get('modified', ''),
        'api_count': len(apis_list),
        'apis': [],
        'common': common_resources,
        'features': features,
        'use_cases': use_cases,
        'integrations': integrations,
        'solutions': solutions,
        'skills': skills,
    }

    # Process individual APIs
    api_entries = []
    for api in apis_list:
        api_aid = api.get('aid', '')
        api_slug = extract_api_slug(api_aid)
        api_name = api.get('name', '')
        api_desc = clean_description(api.get('description', ''))

        provider_data['apis'].append({
            'slug': api_slug,
            'name': api_name,
            'description': api_desc[:200]
        })

        github_raw_base = f"https://raw.githubusercontent.com/api-evangelist/{provider_slug}/refs/heads/main"
        resolved_properties = []
        for prop in api.get('properties', []):
            p = dict(prop)
            url = p.get('url', '')
            if url and not url.startswith('http'):
                p['url'] = f"{github_raw_base}/{url}"
            resolved_properties.append(p)

        # Prefer the API's OpenAPI spec for the source widget; fall back to
        # AsyncAPI / Postman; last resort is the apis.yml entry itself.
        spec_pref = [
            ('openapi', 'OpenAPI Specification'),
            ('asyncapi', 'AsyncAPI Specification'),
            ('postman', 'Postman Collection'),
            ('postman collection', 'Postman Collection'),
        ]
        spec_text = None
        spec_url = None
        spec_format = None
        spec_heading = None
        spec_filename = None
        for ptype_target, heading in spec_pref:
            for prop in api.get('properties', []) or []:
                if (prop.get('type') or '').lower() != ptype_target:
                    continue
                purl = prop.get('url') or ''
                if not purl:
                    continue
                if purl.startswith('http'):
                    # External URL — record it directly; the source widget will
                    # lazy-fetch the content on page load rather than inlining it.
                    clean = purl.split('?')[0]
                    ext = os.path.splitext(clean)[1].lower()
                    spec_format = 'json' if ext == '.json' else 'yaml'
                    spec_url = purl
                    spec_heading = heading
                    spec_filename = os.path.basename(clean) or (ptype_target + '.yaml')
                    break
                local_path = os.path.join(provider_dir, purl)
                resolved_purl = purl
                if not os.path.exists(local_path):
                    # Try fallbacks for malformed paths in apis.yml:
                    # 1) Some providers (Stripe, Mastercard, Microsoft Graph,
                    #    Anthropic, SendGrid, OpenAI, etc.) reference OpenAPI
                    #    specs at properties/<file> but ship the actual file
                    #    at openapi/<file>.
                    # 2) Some providers (Microsoft Azure, Walmart) have
                    #    apis.yml entries like "openapifoo.yml" missing the
                    #    slash — `openapi<filename>` instead of `openapi/<filename>`.
                    fallback_dirs = ['openapi', 'asyncapi', 'postman']
                    candidate_path = None
                    candidate_purl = None

                    # Pattern (2): no-slash prefix
                    for d in fallback_dirs:
                        if purl.startswith(d) and not purl.startswith(d + '/'):
                            rest = purl[len(d):]
                            cand = os.path.join(provider_dir, d, rest)
                            if os.path.exists(cand):
                                candidate_path = cand
                                candidate_purl = f"{d}/{rest}"
                                break

                    # Pattern (1): wrong dir, same basename
                    if candidate_path is None:
                        basename = os.path.basename(purl)
                        for d in fallback_dirs:
                            cand = os.path.join(provider_dir, d, basename)
                            if os.path.exists(cand):
                                candidate_path = cand
                                candidate_purl = f"{d}/{basename}"
                                break

                    if candidate_path is None:
                        continue
                    local_path = candidate_path
                    resolved_purl = candidate_purl
                try:
                    with open(local_path) as fh:
                        spec_text = fh.read()
                except OSError:
                    continue
                ext = os.path.splitext(resolved_purl)[1].lower()
                spec_format = 'json' if ext == '.json' else 'yaml'
                spec_url = f"{github_raw_base}/{resolved_purl}"
                spec_heading = heading
                spec_filename = os.path.basename(resolved_purl)
                break
            if spec_text or spec_url:
                break

        # Auto-discover: if apis.yml didn't list a spec property but the provider
        # ships an exactly-named OpenAPI in openapi/<slug>{.yml,.yaml,.json} or
        # openapi/<slug>-openapi.{yml,yaml,json}, link it. Exact-match only —
        # fuzzy matching risks attaching the wrong spec to the wrong API.
        if not (spec_text or spec_url):
            for rel in (
                f"openapi/{api_slug}.yml",
                f"openapi/{api_slug}.yaml",
                f"openapi/{api_slug}.json",
                f"openapi/{api_slug}-openapi.yml",
                f"openapi/{api_slug}-openapi.yaml",
                f"openapi/{api_slug}-openapi.json",
            ):
                local_path = os.path.join(provider_dir, rel)
                if not os.path.exists(local_path):
                    continue
                try:
                    with open(local_path, encoding='utf-8', errors='replace') as fh:
                        spec_text = fh.read()
                except Exception:
                    continue
                spec_format = 'json' if rel.endswith('.json') else 'yaml'
                spec_url = f"{github_raw_base}/{rel}"
                spec_heading = 'OpenAPI Specification'
                spec_filename = os.path.basename(rel)
                break

        api_data = {
            'layout': 'api',
            'aid': api_aid,
            'slug': api_slug,
            'name': api_name,
            'description': api_desc,
            'provider_slug': provider_slug,
            'provider_name': provider_name,
            'image': api.get('image', ''),
            'humanURL': api.get('humanURL', ''),
            'baseURL': api.get('baseURL', ''),
            'tags': filter_tags(api.get('tags', [])),
            'properties': resolved_properties,
        }
        if spec_text and spec_format == 'json':
            api_data['source_json'] = cap_source(spec_text, spec_url)
            api_data['source_json_url'] = spec_url
            api_data['source_heading'] = spec_heading
            api_data['source_filename'] = spec_filename
        elif spec_text:
            api_data['source_yaml'] = cap_source(spec_text, spec_url)
            api_data['source_yaml_url'] = spec_url
            api_data['source_heading'] = spec_heading
            api_data['source_filename'] = spec_filename
        elif spec_url:
            # Remote URL only — no inline content; widget lazy-fetches on page load.
            url_key = 'source_json_url' if spec_format == 'json' else 'source_yaml_url'
            api_data[url_key] = spec_url
            api_data['source_heading'] = spec_heading
            api_data['source_filename'] = spec_filename
        else:
            # Fallback: dump the API entry from apis.yml so there's still a source view.
            api_source_url = f"{github_raw_base}/apis.yml"
            try:
                api_yaml_str = yaml.dump(api, default_flow_style=False, allow_unicode=True, sort_keys=False, width=100)
                api_data['source_yaml'] = cap_source(api_yaml_str, api_source_url)
                api_data['source_yaml_url'] = api_source_url
                api_data['source_heading'] = 'API entry from apis.yml'
                api_data['source_filename'] = 'apis.yml'
            except Exception:
                pass

        api_filepath = os.path.join(APIS_DIR, provider_slug, f"{api_slug}.md")
        write_frontmatter_file(api_filepath, api_data)
        api_entries.append(api_data)

    # Compute the provider's API spec picker list once and share it across
    # entity types (provider, asyncapi, jsonld, rules) that benefit from it.
    # Schemas are excluded — too many per provider × too many schemas would
    # bloat the schemas repo by hundreds of MB.
    provider_api_specs = []
    for entry in api_entries:
        is_json = 'source_json_url' in entry
        spec_url = entry.get('source_json_url') if is_json else entry.get('source_yaml_url')
        spec_filename = entry.get('source_filename') or ''
        if not spec_url or not spec_filename or spec_filename == 'apis.yml':
            continue
        spec_heading = entry.get('source_heading') or ''
        spec_type = spec_heading.split(' ')[0] if spec_heading else ''
        provider_api_specs.append({
            'slug': entry.get('slug', ''),
            'label': entry.get('name', entry.get('slug', '')),
            'spec_type': spec_type,
            'format': 'json' if is_json else 'yaml',
            'url': spec_url,
            'filename': spec_filename,
        })

    provider_filepath = os.path.join(PROVIDERS_DIR, f"{provider_slug}.md")

    # --- Capabilities ---
    cap_dir = os.path.join(provider_dir, 'capabilities')
    cap_entries = []
    if os.path.isdir(cap_dir):
        cap_files = glob.glob(os.path.join(cap_dir, '*.yaml'))
        for cap_file in sorted(cap_files):
            cap_filename = os.path.basename(cap_file)
            cap_slug = os.path.splitext(cap_filename)[0]

            cap_data = load_yaml(cap_file)
            if not cap_data:
                continue

            info = cap_data.get('info', {})
            cap_label = info.get('label', cap_slug.replace('-', ' ').title())
            cap_desc = clean_description(info.get('description', ''))
            cap_tags = filter_tags(info.get('tags', []))

            operations, tools = extract_operations_from_capability(cap_data)

            workflow = find_matching_workflow(cap_label, vocab_data)
            personas = []
            if workflow:
                persona_ids = workflow.get('personas', [])
                if vocab_data:
                    cap_section = vocab_data.get('capability', {})
                    persona_list = cap_section.get('personas', []) if isinstance(cap_section, dict) else []
                    for pid in persona_ids:
                        for p in persona_list:
                            if not isinstance(p, dict):
                                continue
                            if p.get('id') == pid:
                                personas.append({
                                    'id': pid,
                                    'name': p.get('name', pid),
                                    'description': clean_description(p.get('description', ''))
                                })
                                break

            capability_block = cap_data.get('capability', {})
            consumed_apis = []
            cap_github_raw_base = f"https://raw.githubusercontent.com/api-evangelist/{provider_slug}/refs/heads/main"
            cap_specs = []
            for consumed in capability_block.get('consumes', []):
                import_name = consumed.get('import', '')
                if not import_name:
                    continue
                consumed_apis.append(import_name)
                # Try to surface the upstream OpenAPI for this consumed import.
                location = consumed.get('location', '') or ''
                basename = os.path.splitext(os.path.basename(location))[0] if location else ''
                if not basename:
                    continue
                for rel in (
                    f"openapi/{basename}.yml",
                    f"openapi/{basename}.yaml",
                    f"openapi/{basename}.json",
                    f"openapi/{basename}-openapi.yml",
                    f"openapi/{basename}-openapi.yaml",
                    f"openapi/{basename}-openapi.json",
                ):
                    local_path = os.path.join(provider_dir, rel)
                    if not os.path.exists(local_path):
                        continue
                    fmt = 'json' if rel.endswith('.json') else 'yaml'
                    cap_specs.append({
                        'slug': import_name,
                        'label': import_name,
                        'spec_type': 'OpenAPI',
                        'format': fmt,
                        'url': f"{cap_github_raw_base}/{rel}",
                        'filename': os.path.basename(rel),
                    })
                    break

            search_terms = extract_capability_search_terms(cap_data, vocab_data, provider_tags)

            cap_categories = resolve_capability_categories(
                info, provider_slug, cap_slug, category_suggestions or {}
            )

            source_yaml_url = f"https://raw.githubusercontent.com/api-evangelist/{provider_slug}/refs/heads/main/capabilities/{cap_filename}"
            try:
                with open(cap_file) as fh:
                    raw_yaml = cap_source(fh.read(), source_yaml_url)
            except OSError:
                raw_yaml = ''

            cap_entry = {
                'layout': 'capability',
                'slug': cap_slug,
                'name': cap_label,
                'description': cap_desc,
                'provider_slug': provider_slug,
                'provider_name': provider_name,
                'tags': cap_tags,
                'categories': cap_categories,
                'operations': operations,
                'tools': tools,
                'personas': personas,
                'consumed_apis': consumed_apis,
                'search_terms': search_terms,
                'source_yaml': raw_yaml,
                'source_yaml_url': source_yaml_url,
                'source_filename': cap_filename,
                'source_heading': 'Capability Spec',
            }
            if cap_specs:
                cap_entry['api_specs'] = cap_specs

            cap_filepath = os.path.join(CAPABILITIES_DIR, provider_slug, f"{cap_slug}.md")
            write_frontmatter_file(cap_filepath, cap_entry)
            cap_entries.append(cap_entry)

            if category_implementations is not None and cap_categories:
                impl = {
                    'provider_slug': provider_slug,
                    'provider_name': provider_name,
                    'capability_slug': cap_slug,
                    'capability_name': cap_label,
                    'capability_url': f"https://capabilities.apis.io/capabilities/{provider_slug}/{cap_slug}/",
                    'operation_count': len(operations),
                    'tool_count': len(tools),
                    'consumed_api_count': len(consumed_apis),
                    'tags': cap_tags,
                }
                for cat in cap_categories:
                    category_implementations.setdefault(cat, []).append(impl)

        provider_data['capabilities'] = [
            {'slug': c['slug'], 'name': c['name'], 'description': c['description'][:200]}
            for c in cap_entries
        ]

    # --- Schemas ---
    schema_dir = os.path.join(provider_dir, 'json-schema')
    if os.path.isdir(schema_dir):
        schema_files = glob.glob(os.path.join(schema_dir, '*.json'))
        for schema_file in sorted(schema_files):
            schema_filename = os.path.basename(schema_file)
            schema_slug = extract_schema_slug(schema_filename)

            try:
                schema_data = load_json(schema_file)
            except (json.JSONDecodeError, IOError):
                continue

            title = schema_data.get('title', schema_slug.replace('-', ' ').title())
            desc = clean_description(schema_data.get('description', ''))

            props = schema_data.get('properties', {})
            properties_list = []
            for prop_name, prop_def in props.items():
                if isinstance(prop_def, dict):
                    properties_list.append({
                        'name': prop_name,
                        'type': prop_def.get('type', 'object'),
                        'description': clean_description(prop_def.get('description', ''))[:200]
                    })
                else:
                    properties_list.append({
                        'name': prop_name,
                        'type': str(prop_def) if prop_def else 'unknown',
                        'description': ''
                    })

            schema_source_url = f"https://raw.githubusercontent.com/api-evangelist/{provider_slug}/refs/heads/main/json-schema/{schema_filename}"
            try:
                with open(schema_file) as fh:
                    raw_schema = cap_source(fh.read(), schema_source_url)
            except OSError:
                raw_schema = ''

            schema_entry = {
                'layout': 'schema',
                'slug': schema_slug,
                'title': title,
                'name': title,
                'description': desc,
                'provider_slug': provider_slug,
                'provider_name': provider_name,
                'properties_list': properties_list,
                'tags': provider_tags,
                'schema_file': f"json-schema/{schema_filename}",
                'source_json': raw_schema,
                'source_json_url': schema_source_url,
                'source_heading': 'JSON Schema',
                'source_filename': schema_filename,
            }

            schema_filepath = os.path.join(SCHEMAS_DIR, provider_slug, f"{schema_slug}.md")
            write_frontmatter_file(schema_filepath, schema_entry)

    # --- AsyncAPI Specs ---
    asyncapi_dir = os.path.join(provider_dir, 'asyncapi')
    asyncapi_entries = []
    if os.path.isdir(asyncapi_dir):
        asyncapi_files = glob.glob(os.path.join(asyncapi_dir, '*.yml')) + glob.glob(os.path.join(asyncapi_dir, '*.yaml'))
        for asyncapi_file in sorted(asyncapi_files):
            asyncapi_filename = os.path.basename(asyncapi_file)
            asyncapi_slug = os.path.splitext(asyncapi_filename)[0]

            try:
                asyncapi_data = load_yaml(asyncapi_file)
            except Exception:
                continue
            if not asyncapi_data:
                continue

            info = asyncapi_data.get('info', {})
            title = info.get('title', asyncapi_slug.replace('-', ' ').title())
            desc = clean_description(info.get('description', ''))
            version = info.get('version', '')

            channels = []
            for channel_name, channel_def in asyncapi_data.get('channels', {}).items():
                channel_info = {
                    'name': channel_name,
                    'description': clean_description(channel_def.get('description', '')),
                }
                for op_type in ('publish', 'subscribe'):
                    op = channel_def.get(op_type)
                    if op:
                        channel_info['operation'] = op_type
                        channel_info['operation_id'] = op.get('operationId', '')
                        channel_info['summary'] = clean_description(op.get('summary', ''))
                        break
                channels.append(channel_info)

            messages = []
            for msg_name, msg_def in asyncapi_data.get('components', {}).get('messages', {}).items():
                messages.append({
                    'name': msg_name,
                    'title': msg_def.get('title', msg_name),
                    'summary': clean_description(msg_def.get('summary', '')),
                    'description': clean_description(msg_def.get('description', ''))[:300],
                })

            servers = []
            for srv_name, srv_def in asyncapi_data.get('servers', {}).items():
                servers.append({
                    'name': srv_name,
                    'url': srv_def.get('url', ''),
                    'protocol': srv_def.get('protocol', ''),
                    'description': clean_description(srv_def.get('description', '')),
                })

            github_raw_base = f"https://raw.githubusercontent.com/api-evangelist/{provider_slug}/refs/heads/main"

            asyncapi_source_url = f"{github_raw_base}/asyncapi/{asyncapi_filename}"
            try:
                with open(asyncapi_file) as fh:
                    raw_async = cap_source(fh.read(), asyncapi_source_url)
            except OSError:
                raw_async = ''

            asyncapi_entry = {
                'layout': 'asyncapi',
                'slug': asyncapi_slug,
                'name': title,
                'description': desc,
                'version': version,
                'provider_slug': provider_slug,
                'provider_name': provider_name,
                'tags': provider_tags + ['AsyncAPI', 'Webhooks', 'Events'],
                'channels': channels,
                'messages': messages,
                'servers': servers,
                'spec_file': f"asyncapi/{asyncapi_filename}",
                'spec_url': f"{github_raw_base}/asyncapi/{asyncapi_filename}",
                'source_yaml': raw_async,
                'source_yaml_url': asyncapi_source_url,
                'source_heading': 'AsyncAPI Specification',
                'source_filename': asyncapi_filename,
            }
            if provider_api_specs:
                asyncapi_entry['api_specs'] = provider_api_specs

            asyncapi_filepath = os.path.join(ASYNCAPIS_DIR, provider_slug, f"{asyncapi_slug}.md")
            write_frontmatter_file(asyncapi_filepath, asyncapi_entry)
            asyncapi_entries.append(asyncapi_entry)

    if asyncapi_entries:
        provider_data['asyncapis'] = [
            {'slug': a['slug'], 'name': a['name'], 'description': a['description'][:200]}
            for a in asyncapi_entries
        ]

    # --- JSON-LD Contexts ---
    jsonld_dir = os.path.join(provider_dir, 'json-ld')
    jsonld_entries = []
    if os.path.isdir(jsonld_dir):
        jsonld_files = glob.glob(os.path.join(jsonld_dir, '*.jsonld'))
        for jsonld_file in sorted(jsonld_files):
            jsonld_filename = os.path.basename(jsonld_file)
            jsonld_slug = os.path.splitext(jsonld_filename)[0]

            try:
                jsonld_data = load_json(jsonld_file)
            except (json.JSONDecodeError, IOError):
                continue

            context = jsonld_data.get('@context', {})
            namespaces = []
            classes = []
            properties = []

            for key, value in context.items():
                if key.startswith('@'):
                    continue
                if isinstance(value, str):
                    if '://' in value:
                        namespaces.append({'prefix': key, 'uri': value})
                    else:
                        classes.append(key)
                elif isinstance(value, dict):
                    prop_type = value.get('@type', '')
                    if prop_type.startswith('xsd:'):
                        prop_type = prop_type[4:]
                    elif prop_type == '@id':
                        prop_type = 'reference'
                    container = value.get('@container', '')
                    if container:
                        container = container.replace('@', '')
                    properties.append({
                        'name': key,
                        'type': prop_type,
                        'container': container,
                    })

            title = jsonld_slug.replace('-', ' ').title()
            title = title.replace('Context', '').replace('  ', ' ').strip()
            if not title:
                title = jsonld_slug

            github_raw_base = f"https://raw.githubusercontent.com/api-evangelist/{provider_slug}/refs/heads/main"

            jsonld_source_url = f"{github_raw_base}/json-ld/{jsonld_filename}"
            try:
                with open(jsonld_file) as fh:
                    raw_jsonld = cap_source(fh.read(), jsonld_source_url)
            except OSError:
                raw_jsonld = ''

            jsonld_entry = {
                'layout': 'jsonld',
                'slug': jsonld_slug,
                'name': f"{title} Context",
                'description': f"JSON-LD context defining the semantic vocabulary for {title} from {provider_name}.",
                'provider_slug': provider_slug,
                'provider_name': provider_name,
                'tags': provider_tags + ['JSON-LD', 'Linked Data', 'Semantic Web'],
                'namespaces': namespaces,
                'classes': classes,
                'properties': properties,
                'class_count': len(classes),
                'property_count': len(properties),
                'context_file': f"json-ld/{jsonld_filename}",
                'context_url': f"{github_raw_base}/json-ld/{jsonld_filename}",
                'source_json': raw_jsonld,
                'source_json_url': jsonld_source_url,
                'source_heading': 'JSON-LD Document',
                'source_filename': jsonld_filename,
            }
            if provider_api_specs:
                jsonld_entry['api_specs'] = provider_api_specs

            jsonld_filepath = os.path.join(JSONLD_DIR, provider_slug, f"{jsonld_slug}.md")
            write_frontmatter_file(jsonld_filepath, jsonld_entry)
            jsonld_entries.append(jsonld_entry)

    if jsonld_entries:
        provider_data['jsonld'] = [
            {'slug': j['slug'], 'name': j['name'], 'class_count': j['class_count'], 'property_count': j['property_count']}
            for j in jsonld_entries
        ]

    # --- Spectral Rules ---
    rules_dir = os.path.join(provider_dir, 'rules')
    rules_entries = []
    if os.path.isdir(rules_dir):
        rules_files = glob.glob(os.path.join(rules_dir, '*.yml')) + glob.glob(os.path.join(rules_dir, '*.yaml'))
        for rules_file in sorted(rules_files):
            rules_filename = os.path.basename(rules_file)
            rules_slug = os.path.splitext(rules_filename)[0]

            try:
                rules_data = load_yaml(rules_file)
            except Exception:
                continue
            if not rules_data:
                continue

            raw_rules = rules_data.get('rules', {})
            rules_list = []
            severity_counts = {'error': 0, 'warn': 0, 'info': 0, 'hint': 0}
            categories = set()

            for rule_name, rule_def in raw_rules.items():
                if not isinstance(rule_def, dict):
                    continue
                severity = rule_def.get('severity', 'warn')
                severity_counts[severity] = severity_counts.get(severity, 0) + 1

                parts = rule_name.split('-')
                if len(parts) >= 2:
                    categories.add(parts[0])

                rules_list.append({
                    'name': rule_name,
                    'description': clean_description(rule_def.get('description', '')),
                    'severity': severity,
                    'given': rule_def.get('given', ''),
                })

            title = rules_slug.replace('-', ' ').title()
            github_raw_base = f"https://raw.githubusercontent.com/api-evangelist/{provider_slug}/refs/heads/main"

            rules_entry = {
                'layout': 'rules',
                'slug': rules_slug,
                'name': f"{provider_name} API Rules",
                'description': f"Spectral linting rules defining API design standards and conventions for {provider_name}.",
                'provider_slug': provider_slug,
                'provider_name': provider_name,
                'tags': provider_tags + ['Spectral', 'Linting', 'API Governance'],
                'rules': rules_list,
                'rule_count': len(rules_list),
                'severity_counts': severity_counts,
                'categories': sorted(categories),
                'rules_file': f"rules/{rules_filename}",
                'rules_url': f"{github_raw_base}/rules/{rules_filename}",
            }

            rules_source_url = f"{github_raw_base}/rules/{rules_filename}"
            try:
                with open(rules_file) as fh:
                    raw_rules_text = cap_source(fh.read(), rules_source_url)
            except OSError:
                raw_rules_text = ''
            rules_entry['source_yaml'] = raw_rules_text
            rules_entry['source_yaml_url'] = rules_source_url
            rules_entry['source_heading'] = 'Spectral Ruleset'
            rules_entry['source_filename'] = rules_filename
            if provider_api_specs:
                rules_entry['api_specs'] = provider_api_specs

            rules_filepath = os.path.join(RULES_DIR, provider_slug, f"{rules_slug}.md")
            write_frontmatter_file(rules_filepath, rules_entry)
            rules_entries.append(rules_entry)

    if rules_entries:
        provider_data['rules'] = [
            {'slug': r['slug'], 'name': r['name'], 'rule_count': r['rule_count'], 'severity_counts': r['severity_counts']}
            for r in rules_entries
        ]

    # ---- Plans / Rate Limits / FinOps ----
    # Each provider can publish API Commons Plans, Rate Limits, and FOCUS-aligned
    # FinOps profiles in their respective subdirs. These get aggregated into
    # plans.apis.io, rate-limits.apis.io, finops.apis.io.

    plans_entries = _process_provider_subdir(
        provider_dir, provider_slug, provider_name, provider_data, provider_api_specs,
        github_raw_base, subdir='plans', out_dir=PLANS_DIR, layout='plan',
        source_heading='Pricing Plans',
        derive_meta=_derive_plans_meta,
    )
    if plans_entries:
        provider_data['plans'] = [
            {'slug': p['slug'], 'name': p['name'], 'plan_count': p.get('plan_count', 0)}
            for p in plans_entries
        ]

    ratelimits_entries = _process_provider_subdir(
        provider_dir, provider_slug, provider_name, provider_data, provider_api_specs,
        github_raw_base, subdir='rate-limits', out_dir=RATELIMITS_DIR, layout='ratelimit',
        source_heading='Rate Limits',
        derive_meta=_derive_ratelimits_meta,
    )
    if ratelimits_entries:
        provider_data['rate_limits'] = [
            {'slug': r['slug'], 'name': r['name'], 'limit_count': r.get('limit_count', 0)}
            for r in ratelimits_entries
        ]

    finops_entries = _process_provider_subdir(
        provider_dir, provider_slug, provider_name, provider_data, provider_api_specs,
        github_raw_base, subdir='finops', out_dir=FINOPS_DIR, layout='finops',
        source_heading='FinOps Profile',
        derive_meta=_derive_finops_meta,
    )
    if finops_entries:
        provider_data['finops'] = [
            {'slug': f['slug'], 'name': f['name'], 'service_category': f.get('service_category', '')}
            for f in finops_entries
        ]

    # Apply icon override from manifest
    if icon_manifest and provider_slug in icon_manifest:
        provider_data['image'] = f"/assets/icons/{provider_slug}.png"

    # Embed source apis.yml for the YAML widget (size-capped for big files)
    provider_source_url = (
        f"https://raw.githubusercontent.com/api-evangelist/{provider_slug}/refs/heads/main/apis.yml"
    )
    try:
        with open(apis_yml_path) as fh:
            provider_data['source_yaml'] = cap_source(fh.read(), provider_source_url)
    except OSError:
        provider_data['source_yaml'] = ''
    provider_data['source_yaml_url'] = provider_source_url
    provider_data['source_filename'] = 'apis.yml'
    provider_data['source_heading'] = 'Sources'

    # Picker: reuse the provider_api_specs list computed earlier so the
    # widget can swap between apis.yml and per-API specs on demand.
    if provider_api_specs:
        provider_data['api_specs'] = provider_api_specs

    # Write provider file once with all data
    write_frontmatter_file(provider_filepath, provider_data)

    return provider_data


# RFC 9727 api-catalog property type -> linkset relation + media type
PROPERTY_TYPE_MAP = {
    'OpenAPI':           ('service-desc', 'application/vnd.oai.openapi'),
    'AsyncAPI':          ('service-desc', 'application/vnd.aai.asyncapi'),
    'Postman':           ('service-desc', 'application/vnd.postman.collection+json'),
    'Postman Collection':('service-desc', 'application/vnd.postman.collection+json'),
    'Documentation':     ('service-doc',  'text/html'),
    'JSON Schema':       ('describedby',  'application/schema+json'),
    'Schema':            ('describedby',  'application/schema+json'),
    'JSON-LD':           ('describedby',  'application/ld+json'),
}


def build_api_catalogs():
    """Generate RFC 9727 /.well-known/api-catalog linksets for apis & providers sites."""
    by_provider = {}
    for provider_dir in sorted(glob.glob(os.path.join(APIS_DIR, '*'))):
        if not os.path.isdir(provider_dir):
            continue
        provider_slug = os.path.basename(provider_dir)
        for api_md in sorted(glob.glob(os.path.join(provider_dir, '*.md'))):
            with open(api_md) as fh:
                text = fh.read()
            if not text.startswith('---\n'):
                continue
            end = text.find('\n---\n', 4)
            if end == -1:
                continue
            try:
                fm = yaml.safe_load(text[4:end]) or {}
            except yaml.YAMLError:
                continue
            by_provider.setdefault(provider_slug, []).append(fm)

    def api_links(fm):
        sd, doc, db = [], [], []
        for prop in fm.get('properties', []) or []:
            url = prop.get('url')
            ptype = prop.get('type', '')
            if not url:
                continue
            rel, media = PROPERTY_TYPE_MAP.get(ptype, ('describedby', None))
            link = {'href': url}
            if media:
                link['type'] = media
            if ptype and ptype not in PROPERTY_TYPE_MAP:
                link['title'] = ptype
            {'service-desc': sd, 'service-doc': doc, 'describedby': db}[rel].append(link)
        if fm.get('humanURL') and not any(d['href'] == fm['humanURL'] for d in doc):
            doc.append({'href': fm['humanURL'], 'type': 'text/html'})
        return sd, doc, db

    apis_linkset = []
    for provider_slug in sorted(by_provider):
        for fm in by_provider[provider_slug]:
            api_slug = fm.get('slug', '')
            if not api_slug:
                continue
            sd, doc, db = api_links(fm)
            if not (sd or doc or db):
                continue
            entry = {'anchor': f"https://apis.apis.io/apis/{provider_slug}/{api_slug}/"}
            if fm.get('name'):
                entry['title'] = fm['name']
            if sd: entry['service-desc'] = sd
            if doc: entry['service-doc'] = doc
            if db: entry['describedby'] = db
            apis_linkset.append(entry)

    apis_wk = os.path.join(ROOT_DIR, 'apis', '.well-known')
    os.makedirs(apis_wk, exist_ok=True)
    apis_catalog = {'linkset': apis_linkset}
    for fname in ('api-catalog', 'api-catalog.json'):
        with open(os.path.join(apis_wk, fname), 'w') as fh:
            json.dump(apis_catalog, fh, indent=2)

    providers_linkset = []
    for provider_slug in sorted(by_provider):
        anchor = f"https://providers.apis.io/providers/{provider_slug}/"
        sd, doc, db = [], [], []
        for fm in by_provider[provider_slug]:
            psd, pdoc, pdb = api_links(fm)
            for link in psd:
                link = dict(link)
                link.setdefault('title', fm.get('name', ''))
                sd.append(link)
            for link in pdoc:
                link = dict(link)
                link.setdefault('title', fm.get('name', ''))
                doc.append(link)
        entry = {'anchor': anchor, 'title': provider_slug}
        if sd: entry['service-desc'] = sd
        if doc: entry['service-doc'] = doc
        providers_linkset.append(entry)

    providers_wk = os.path.join(ROOT_DIR, 'providers', '.well-known')
    os.makedirs(providers_wk, exist_ok=True)
    providers_catalog = {'linkset': providers_linkset}
    for fname in ('api-catalog', 'api-catalog.json'):
        with open(os.path.join(providers_wk, fname), 'w') as fh:
            json.dump(providers_catalog, fh, indent=2)

    print(f"api-catalog:  {len(apis_linkset)} APIs ({sum(1 for e in apis_linkset if 'service-desc' in e)} with machine description), {len(providers_linkset)} providers")


def clear_collections():
    """Remove existing collection directories."""
    for d in [PROVIDERS_DIR, APIS_DIR, CAPABILITIES_DIR, CATEGORIES_DIR,
              SCHEMAS_DIR, ASYNCAPIS_DIR, JSONLD_DIR, RULES_DIR]:
        if os.path.exists(d):
            shutil.rmtree(d)
        os.makedirs(d, exist_ok=True)
    print("Cleared existing collections.")


def load_canonical_capabilities():
    """Load the seed taxonomy keyed by slug."""
    if not os.path.exists(CANONICAL_CAPS_PATH):
        return {}
    rows = load_yaml(CANONICAL_CAPS_PATH) or []
    return {r['slug']: r for r in rows if isinstance(r, dict) and r.get('slug')}


def load_category_suggestions():
    """Return {(provider_slug, cap_slug): [category_slug, ...]} from suggestions
    file. Only the top candidate above MIN_FALLBACK_SUGGESTION_SCORE is used."""
    if not os.path.exists(CATEGORY_SUGGESTIONS_PATH):
        return {}
    rows = load_yaml(CATEGORY_SUGGESTIONS_PATH) or []
    out = {}
    for r in rows:
        if not isinstance(r, dict):
            continue
        cands = r.get('candidates') or []
        chosen = []
        for c in cands[:1]:
            if isinstance(c, dict) and c.get('score', 0) >= MIN_FALLBACK_SUGGESTION_SCORE:
                chosen.append(c['category'])
        if chosen:
            out[(r.get('provider', ''), r.get('slug', ''))] = chosen
    return out


def resolve_capability_categories(info, provider_slug, cap_slug, suggestions):
    """Pick categories: explicit info.categories wins; else fall back to suggestions."""
    explicit = info.get('categories') or []
    if isinstance(explicit, list) and explicit:
        return [c for c in explicit if isinstance(c, str)]
    return suggestions.get((provider_slug, cap_slug), [])


def build_category_pages(canonicals, implementations):
    """Emit one Jekyll page per canonical capability that has implementations."""
    os.makedirs(CATEGORIES_DIR, exist_ok=True)
    pages = 0
    total_impls = 0
    for slug in sorted(canonicals.keys()):
        canonical = canonicals[slug]
        impls = sorted(
            implementations.get(slug, []),
            key=lambda i: (i['provider_slug'], i['capability_slug']),
        )
        if not impls:
            continue
        provider_count = len({i['provider_slug'] for i in impls})
        page = {
            'layout': 'category',
            'slug': slug,
            'name': canonical.get('name', slug),
            'short': canonical.get('short', ''),
            'description': canonical.get('description', ''),
            'domain': canonical.get('domain', ''),
            'common_operations': canonical.get('common_operations', []) or [],
            'related': canonical.get('related', []) or [],
            'aliases': canonical.get('aliases', []) or [],
            'implementations': impls,
            'implementation_count': len(impls),
            'provider_count': provider_count,
        }
        write_frontmatter_file(os.path.join(CATEGORIES_DIR, f"{slug}.md"), page)
        pages += 1
        total_impls += len(impls)
    print(f"Categories:   {pages} category pages, {total_impls} implementations")
    return pages, total_impls


def copy_shared_assets():
    """Copy shared layouts and assets to all subdomain repos."""
    import subprocess
    # Run the bootstrap script to copy shared assets
    bootstrap_script = os.path.join(SCRIPT_DIR, 'bootstrap-sites.py')
    if os.path.exists(bootstrap_script):
        subprocess.run([sys.executable, bootstrap_script], check=True)


def build_vocabulary_index(provider_dirs):
    """Build a consolidated vocabulary index from all provider repos."""
    all_resources = []
    all_actions = []
    all_personas = []
    all_domains = []
    all_schemas_vocab = []
    all_tags = set()
    provider_count = 0

    for provider_dir in provider_dirs:
        vocab_files = glob.glob(os.path.join(provider_dir, 'vocabulary', '*-vocabulary.yaml'))
        if not vocab_files:
            continue

        vocab_data = load_yaml(vocab_files[0])
        if not vocab_data:
            continue

        is_structured = 'vocabulary' in vocab_data or 'operational' in vocab_data

        if is_structured:
            info = vocab_data.get('info', {})
            provider_name = info.get('provider', os.path.basename(provider_dir))
        else:
            provider_name = vocab_data.get('provider', vocab_data.get('name', os.path.basename(provider_dir)))

        provider_slug = os.path.basename(provider_dir)
        provider_count += 1

        if is_structured:
            operational = vocab_data.get('operational', {})

            for res in operational.get('resources', []):
                if not isinstance(res, dict):
                    continue
                all_resources.append({
                    'name': res.get('name', ''),
                    'description': clean_description(res.get('description', '')),
                    'provider': provider_name,
                    'provider_slug': provider_slug,
                    'actions': res.get('actions', []),
                    'apis': res.get('apis', []),
                })

            for action in operational.get('actions', []):
                if not isinstance(action, dict):
                    continue
                all_actions.append({
                    'name': action.get('name', ''),
                    'verb': action.get('verb', ''),
                    'pattern': action.get('pattern', ''),
                    'description': clean_description(action.get('description', '')),
                    'provider': provider_name,
                    'provider_slug': provider_slug,
                })

            schemas_section = operational.get('schemas', {})
            if isinstance(schemas_section, dict):
                for category, schema_list in schemas_section.items():
                    if isinstance(schema_list, list):
                        for s in schema_list:
                            if not isinstance(s, dict):
                                continue
                            all_schemas_vocab.append({
                                'name': s.get('name', ''),
                                'description': clean_description(s.get('description', '')),
                                'category': category,
                                'provider': provider_name,
                                'provider_slug': provider_slug,
                            })

            cap = vocab_data.get('capability', {})
            if not isinstance(cap, dict):
                cap = {}

            for persona in cap.get('personas', []):
                if not isinstance(persona, dict):
                    continue
                all_personas.append({
                    'id': persona.get('id', ''),
                    'name': persona.get('name', ''),
                    'description': clean_description(persona.get('description', '')),
                    'provider': provider_name,
                    'provider_slug': provider_slug,
                    'workflows': persona.get('workflows', []),
                })

            for domain in cap.get('domains', []):
                if not isinstance(domain, dict):
                    continue
                all_domains.append({
                    'name': domain.get('name', ''),
                    'description': clean_description(domain.get('description', '')),
                    'provider': provider_name,
                    'provider_slug': provider_slug,
                    'resources': domain.get('resources', []),
                })
        else:
            for tag in vocab_data.get('tags', []):
                all_tags.add(tag)

    seen_actions = {}
    for a in all_actions:
        key = a['name']
        if key not in seen_actions:
            seen_actions[key] = {
                'name': a['name'],
                'verb': a['verb'],
                'pattern': a['pattern'],
                'description': a['description'],
                'providers': [a['provider']],
            }
        else:
            if a['provider'] not in seen_actions[key]['providers']:
                seen_actions[key]['providers'].append(a['provider'])

    return {
        'resources': all_resources,
        'actions': list(seen_actions.values()),
        'personas': all_personas,
        'domains': all_domains,
        'schemas': all_schemas_vocab,
        'tags': sorted(all_tags),
        'stats': {
            'providers': provider_count,
            'resources': len(all_resources),
            'actions': len(seen_actions),
            'personas': len(all_personas),
            'domains': len(all_domains),
            'schemas': len(all_schemas_vocab),
        }
    }


def pull_all_provider_repos():
    """Refresh the provider mirror with git pull --ff-only before building.

    Skipped if SKIP_PULL=1 is set in the environment. The mirror is the source
    of truth for the build; if it's stale, the network publishes stale content
    even when GitHub Pages successfully rebuilds.
    """
    if os.environ.get('SKIP_PULL') == '1':
        print("Skipping provider-repo pull (SKIP_PULL=1)")
        return
    import subprocess
    pull_script = os.path.join(SCRIPT_DIR, 'pull-all.sh')
    if not os.path.exists(pull_script):
        print(f"WARNING: pull-all.sh not found at {pull_script}; skipping pull")
        return
    print(f"\nRefreshing provider mirror at {EVANGELIST_DIR}...")
    env = os.environ.copy()
    env['EVANGELIST_DIR'] = EVANGELIST_DIR
    subprocess.run(['bash', pull_script], env=env, check=False)


def main():
    print("=== APIs.io Build Script (Subdomain Architecture) ===")
    print(f"Source: {EVANGELIST_DIR}")
    print(f"Output: {ROOT_DIR}")

    if not os.path.isdir(EVANGELIST_DIR):
        print(f"ERROR: api-evangelist directory not found at {EVANGELIST_DIR}")
        sys.exit(1)

    pull_all_provider_repos()

    # Discover provider repos
    provider_dirs = sorted([
        os.path.join(EVANGELIST_DIR, d)
        for d in os.listdir(EVANGELIST_DIR)
        if os.path.isdir(os.path.join(EVANGELIST_DIR, d))
        and os.path.exists(os.path.join(EVANGELIST_DIR, d, 'apis.yml'))
    ])

    if not provider_dirs:
        print("ERROR: No provider repos found with apis.yml")
        sys.exit(1)

    print(f"Found {len(provider_dirs)} provider(s)")

    # Copy shared assets to all sites
    print("\nCopying shared assets to subdomain sites...")
    copy_shared_assets()

    # Copy icon assets to providers site (icons live with providers)
    icons_src = os.path.join(NETWORK_DIR, 'assets', 'icons')
    icons_dst = os.path.join(ROOT_DIR, 'providers', 'assets', 'icons')
    if os.path.isdir(icons_src):
        if os.path.exists(icons_dst):
            shutil.rmtree(icons_dst)
        shutil.copytree(icons_src, icons_dst)
        print(f"Copied icons to providers site")

    # Load icon manifest
    icons_manifest_path = os.path.join(NETWORK_DIR, 'assets', 'icons', 'manifest.json')
    icon_manifest = {}
    if os.path.exists(icons_manifest_path):
        with open(icons_manifest_path) as f:
            icon_manifest = json.load(f)
        print(f"Icon manifest: {len(icon_manifest)} icon(s)")

    # Clear and rebuild
    clear_collections()

    # Load canonical capability taxonomy + auto-suggested fallback mappings.
    canonical_capabilities = load_canonical_capabilities()
    category_suggestions = load_category_suggestions()
    category_implementations = {}
    print(f"Canonical capabilities: {len(canonical_capabilities)} entries; "
          f"{len(category_suggestions)} fallback suggestions loaded")

    providers = []
    total_apis = 0
    total_caps = 0

    for provider_dir in provider_dirs:
        try:
            result = process_provider(
                provider_dir,
                icon_manifest,
                category_suggestions=category_suggestions,
                category_implementations=category_implementations,
            )
            if result:
                providers.append(result)
                total_apis += result.get('api_count', 0)
                total_caps += len(result.get('capabilities', []))
        except Exception as e:
            print(f"  ERROR processing {os.path.basename(provider_dir)}: {e}")

    # Generate cross-provider category pages.
    if canonical_capabilities:
        build_category_pages(canonical_capabilities, category_implementations)

    # Build vocabulary index -> vocabularies site
    vocab_index = build_vocabulary_index(provider_dirs)
    vocab_dir = os.path.join(ROOT_DIR, 'vocabularies')
    os.makedirs(vocab_dir, exist_ok=True)
    vocab_path = os.path.join(vocab_dir, 'vocabulary.json')
    with open(vocab_path, 'w') as f:
        json.dump(vocab_index, f, indent=2)
    print(f"Vocabulary:   {vocab_index['stats']['providers']} providers, {vocab_index['stats']['resources']} resources, {vocab_index['stats']['personas']} personas, {vocab_index['stats']['domains']} domains")

    # Count file-based collections
    def count_md(d):
        n = 0
        for root, dirs, files in os.walk(d):
            n += len([f for f in files if f.endswith('.md')])
        return n

    total_schemas = count_md(SCHEMAS_DIR)
    total_asyncapis = count_md(ASYNCAPIS_DIR)
    total_jsonld = count_md(JSONLD_DIR)
    total_rules = count_md(RULES_DIR)
    total_categories = count_md(CATEGORIES_DIR)
    total_plans = count_md(PLANS_DIR)
    total_ratelimits = count_md(RATELIMITS_DIR)
    total_finops = count_md(FINOPS_DIR)

    # Write stats to network _data for homepage counts
    network_data_dir = os.path.join(NETWORK_DIR, '_data')
    os.makedirs(network_data_dir, exist_ok=True)
    stats = {
        'providers': len(providers),
        'apis': total_apis,
        'capabilities': total_caps,
        'categories': total_categories,
        'schemas': total_schemas,
        'asyncapis': total_asyncapis,
        'jsonld': total_jsonld,
        'rules': total_rules,
        'plans': total_plans,
        'rate_limits': total_ratelimits,
        'finops': total_finops,
    }
    with open(os.path.join(network_data_dir, 'stats.json'), 'w') as f:
        json.dump(stats, f, indent=2)

    # RFC 9727 api-catalog
    build_api_catalogs()

    print(f"\n=== Build Complete ===")
    print(f"Providers:    {len(providers)}")
    print(f"APIs:         {total_apis}")
    print(f"Capabilities: {total_caps}")
    print(f"Categories:   {total_categories}")
    print(f"Schemas:      {total_schemas}")
    print(f"AsyncAPIs:    {total_asyncapis}")
    print(f"JSON-LD:      {total_jsonld}")
    print(f"Rules:        {total_rules}")
    print(f"Plans:        {total_plans}")
    print(f"Rate Limits:  {total_ratelimits}")
    print(f"FinOps:       {total_finops}")


if __name__ == '__main__':
    main()
