# APIs.io — Federated API Search Network

[**apis.io**](https://apis.io) is a federated, agent-friendly API discovery network. It indexes API providers from across the public internet — their APIs, capabilities, schemas, event-driven specs, governance rules, vocabularies, and JSON-LD contexts — and exposes each slice of metadata at its own subdomain. This repo is the hub: the homepage, the blog, the build pipeline, and the cross-network stats.

**Live site:** [https://apis.io](https://apis.io)

## What's in this repo

- **`index.html`, `_layouts/`, `_includes/`, `assets/`** — the apis.io homepage and shared site chrome
- **`_posts/`** — the apis.io blog (network updates, provider profiles, weekly roundups)
- **`_data/`** — cross-network data including `stats.json` (the homepage counts), canonical capabilities, and category suggestions
- **`scripts/build.py`** — the build pipeline. Reads from the [api-evangelist](https://github.com/api-evangelist) provider repos and emits Jekyll collections into every other site repo in the network. Run with `EVANGELIST_DIR=/path/to/provider/repos python3 scripts/build.py`.
- **`scripts/generate-blog-images.py`** — generates banner images for blog posts via Gemini Imagen
- **`scripts/generate-icons.py`**, **`scripts/suggest-categories.py`**, **`scripts/diff-stats.py`** — supporting tooling for the network

## How the network is built

The build pipeline reads a directory of [api-evangelist](https://github.com/api-evangelist) provider repositories — each one a Git-versioned APIs.json profile of a single API provider — and produces:

- Provider, API, capability, schema, AsyncAPI, JSON-LD, and rule records as Jekyll markdown
- A federated [api-catalog](https://apis.apis.io/.well-known/api-catalog) ([RFC 9727](https://www.rfc-editor.org/rfc/rfc9727.html)) feed
- Search indexes for each subdomain
- Cross-network stats consumed by the homepage

Each subdomain site is its own Git repo and its own Jekyll deploy on GitHub Pages.

## The APIs.io network

| Site | Repo | What it indexes |
|---|---|---|
| [apis.io](https://apis.io) | [network](https://github.com/api-search/network) | Search hub, blog, build pipeline |
| [developer.apis.io](https://developer.apis.io) | [portal](https://github.com/api-search/portal) | Developer portal & feeds |
| [providers.apis.io](https://providers.apis.io) | [providers](https://github.com/api-search/providers) | API provider profiles |
| [apis.apis.io](https://apis.apis.io) | [apis](https://github.com/api-search/apis) | Individual API records |
| [capabilities.apis.io](https://capabilities.apis.io) | [capabilities](https://github.com/api-search/capabilities) | Naftiko capability specs |
| [schemas.apis.io](https://schemas.apis.io) | [schemas](https://github.com/api-search/schemas) | JSON Schemas |
| [asyncapi.apis.io](https://asyncapi.apis.io) | [asyncapi](https://github.com/api-search/asyncapi) | AsyncAPI event-driven specs |
| [json-ld.apis.io](https://json-ld.apis.io) | [json-ld](https://github.com/api-search/json-ld) | JSON-LD contexts |
| [rules.apis.io](https://rules.apis.io) | [rules](https://github.com/api-search/rules) | Spectral governance rules |
| [vocabularies.apis.io](https://vocabularies.apis.io) | [vocabularies](https://github.com/api-search/vocabularies) | Provider vocabularies |
| [tags.apis.io](https://tags.apis.io) | [tags](https://github.com/api-search/tags) | API tag index |
| [examples.apis.io](https://examples.apis.io) | [examples](https://github.com/api-search/examples) | API usage examples |

## Related projects

- [APIs.json](https://apisjson.org) — the machine-readable specification that indexes API operations
- [API Commons](https://apicommons.org) — the standard vocabulary of common operational properties referenced by APIs.json
- [Naftiko](https://github.com/naftiko/framework) — the open-source framework that runs capability specs as REST, MCP, and Agent Skill surfaces
- [api-evangelist](https://github.com/api-evangelist) — the upstream provider profile repos this network is built from

## Support

APIs.io, APIs.json, and API Commons are projects led by Kin Lane and Steve Willmott. Open issues here for site or build questions; open issues at [apisjson.org](https://apisjson.org) or [apicommons.org](https://apicommons.org) for spec-level questions.
