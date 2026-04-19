---
description: The key item containing key metadata.
layout: schema
name: KeyItem
properties_list:
- description: Key identifier.
  name: kid
  type: string
- description: Application specific metadata in the form of key-value pairs.
  name: tags
  type: object
- description: True if the key's lifetime is managed by key vault.
  name: managed
  type: boolean
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-key-item-schema.json
slug: azure-key-vault-data-plane-key-item
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: KeyItem
---
