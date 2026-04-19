---
description: The secret set parameters.
layout: schema
name: SecretSetParameters
properties_list:
- description: The value of the secret.
  name: value
  type: string
- description: Application specific metadata in the form of key-value pairs.
  name: tags
  type: object
- description: Type of the secret value such as a password.
  name: contentType
  type: string
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-secret-set-parameters-schema.json
slug: azure-key-vault-data-plane-secret-set-parameters
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: SecretSetParameters
---
