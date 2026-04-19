---
aid: 1password:1password-connect-api
baseURL: http://localhost:8080
description: The 1Password Connect Server API provides secure access to 1Password items and vaults in your company's apps and cloud infrastructure through a private REST API. Connect Servers bridge the gap between 1Password and your infrastructure by enabling programmatic access to secrets stored in shared vaults. You can create, read, update, and delete items, manage vaults, and retrieve files attached to items.
humanURL: https://developer.1password.com/docs/connect/api-reference/
image: ''
layout: api
name: 1Password Connect Server API
properties:
- type: Documentation
  url: https://developer.1password.com/docs/connect/api-reference/
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/1password/refs/heads/main/openapi/1password-connect-openapi.yml
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/1password/refs/heads/main/json-schema/1password-connect-vault-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/1password/refs/heads/main/json-schema/1password-connect-item-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/1password/refs/heads/main/json-schema/1password-connect-full-item-schema.json
- type: JSON-LD
  url: https://raw.githubusercontent.com/api-evangelist/1password/refs/heads/main/json-ld/1password-connect-context.jsonld
provider_name: 1Password
provider_slug: 1password
slug: 1password-connect-api
tags:
- Items
- Passwords
- Secrets
- Vaults
---
