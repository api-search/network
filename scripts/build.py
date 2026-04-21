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
EVANGELIST_DIR = os.path.join(ROOT_DIR, 'api-evangelist')
SHARED_DIR = os.path.join(NETWORK_DIR, '_shared')

# Output dirs - each goes to its own subdomain repo
PROVIDERS_DIR = os.path.join(ROOT_DIR, 'providers', '_providers')
APIS_DIR = os.path.join(ROOT_DIR, 'apis', '_apis')
CAPABILITIES_DIR = os.path.join(ROOT_DIR, 'capabilities', '_capabilities')
SCHEMAS_DIR = os.path.join(ROOT_DIR, 'schemas', '_schemas')
ASYNCAPIS_DIR = os.path.join(ROOT_DIR, 'asyncapi', '_asyncapis')
JSONLD_DIR = os.path.join(ROOT_DIR, 'json-ld', '_jsonld')
RULES_DIR = os.path.join(ROOT_DIR, 'rules', '_rules')

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


def process_provider(provider_dir, icon_manifest=None):
    """Process a single api-evangelist provider repo."""
    apis_yml_path = os.path.join(provider_dir, 'apis.yml')
    if not os.path.exists(apis_yml_path):
        print(f"  Skipping {provider_dir} - no apis.yml")
        return None

    data = load_yaml(apis_yml_path)
    provider_slug = data.get('aid', os.path.basename(provider_dir))
    provider_name = data.get('name', provider_slug)
    provider_tags = data.get('tags', [])

    print(f"  Processing: {provider_name} ({provider_slug})")

    # Load vocabulary if available
    vocab_data = None
    vocab_files = glob.glob(os.path.join(provider_dir, 'vocabulary', '*-vocabulary.yaml'))
    if vocab_files:
        vocab_data = load_yaml(vocab_files[0])

    # --- Provider ---
    apis_list = data.get('apis', [])
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
            'tags': api.get('tags', []),
            'properties': resolved_properties,
        }

        api_filepath = os.path.join(APIS_DIR, provider_slug, f"{api_slug}.md")
        write_frontmatter_file(api_filepath, api_data)
        api_entries.append(api_data)

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
            cap_tags = info.get('tags', [])

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
            for consumed in capability_block.get('consumes', []):
                import_name = consumed.get('import', '')
                if import_name:
                    consumed_apis.append(import_name)

            search_terms = extract_capability_search_terms(cap_data, vocab_data, provider_tags)

            cap_entry = {
                'layout': 'capability',
                'slug': cap_slug,
                'name': cap_label,
                'description': cap_desc,
                'provider_slug': provider_slug,
                'provider_name': provider_name,
                'tags': cap_tags,
                'operations': operations,
                'tools': tools,
                'personas': personas,
                'consumed_apis': consumed_apis,
                'search_terms': search_terms,
            }

            cap_filepath = os.path.join(CAPABILITIES_DIR, provider_slug, f"{cap_slug}.md")
            write_frontmatter_file(cap_filepath, cap_entry)
            cap_entries.append(cap_entry)

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
            }

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
            }

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

            rules_filepath = os.path.join(RULES_DIR, provider_slug, f"{rules_slug}.md")
            write_frontmatter_file(rules_filepath, rules_entry)
            rules_entries.append(rules_entry)

    if rules_entries:
        provider_data['rules'] = [
            {'slug': r['slug'], 'name': r['name'], 'rule_count': r['rule_count'], 'severity_counts': r['severity_counts']}
            for r in rules_entries
        ]

    # Apply icon override from manifest
    if icon_manifest and provider_slug in icon_manifest:
        provider_data['image'] = f"/assets/icons/{provider_slug}.png"

    # Write provider file once with all data
    write_frontmatter_file(provider_filepath, provider_data)

    return provider_data


def clear_collections():
    """Remove existing collection directories."""
    for d in [PROVIDERS_DIR, APIS_DIR, CAPABILITIES_DIR, SCHEMAS_DIR,
              ASYNCAPIS_DIR, JSONLD_DIR, RULES_DIR]:
        if os.path.exists(d):
            shutil.rmtree(d)
        os.makedirs(d, exist_ok=True)
    print("Cleared existing collections.")


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
                all_resources.append({
                    'name': res.get('name', ''),
                    'description': clean_description(res.get('description', '')),
                    'provider': provider_name,
                    'provider_slug': provider_slug,
                    'actions': res.get('actions', []),
                    'apis': res.get('apis', []),
                })

            for action in operational.get('actions', []):
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


def main():
    print("=== APIs.io Build Script (Subdomain Architecture) ===")
    print(f"Source: {EVANGELIST_DIR}")
    print(f"Output: {ROOT_DIR}")

    if not os.path.isdir(EVANGELIST_DIR):
        print(f"ERROR: api-evangelist directory not found at {EVANGELIST_DIR}")
        sys.exit(1)

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

    providers = []
    total_apis = 0
    total_caps = 0

    for provider_dir in provider_dirs:
        try:
            result = process_provider(provider_dir, icon_manifest)
            if result:
                providers.append(result)
                total_apis += result.get('api_count', 0)
                total_caps += len(result.get('capabilities', []))
        except Exception as e:
            print(f"  ERROR processing {os.path.basename(provider_dir)}: {e}")

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

    print(f"\n=== Build Complete ===")
    print(f"Providers:    {len(providers)}")
    print(f"APIs:         {total_apis}")
    print(f"Capabilities: {total_caps}")
    print(f"Schemas:      {total_schemas}")
    print(f"AsyncAPIs:    {total_asyncapis}")
    print(f"JSON-LD:      {total_jsonld}")
    print(f"Rules:        {total_rules}")


if __name__ == '__main__':
    main()
