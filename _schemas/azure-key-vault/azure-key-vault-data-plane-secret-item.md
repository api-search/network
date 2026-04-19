---
description: The secret item containing secret metadata.
layout: schema
name: SecretItem
properties_list:
- description: Secret identifier.
  name: id
  type: string
- description: Application specific metadata in the form of key-value pairs.
  name: tags
  type: object
- description: Type of the secret value such as a password.
  name: contentType
  type: string
- description: True if the secret's lifetime is managed by key vault.
  name: managed
  type: boolean
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-secret-item-schema.json
slug: azure-key-vault-data-plane-secret-item
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: SecretItem
---
