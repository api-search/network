---
description: The secret list result.
layout: schema
name: SecretListResult
properties_list:
- description: A list of secrets.
  name: value
  type: array
- description: The URL to get the next set of secrets.
  name: nextLink
  type: string
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-secret-list-result-schema.json
slug: azure-key-vault-data-plane-secret-list-result
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: SecretListResult
---
