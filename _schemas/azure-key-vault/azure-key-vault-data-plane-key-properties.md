---
description: Properties of the key pair backing a certificate.
layout: schema
name: KeyProperties
properties_list:
- description: Indicates if the private key can be exported.
  name: exportable
  type: boolean
- description: 'The key size in bits. For example: 2048, 3072, or 4096 for RSA.'
  name: key_size
  type: integer
- description: Indicates if the same key pair will be used on certificate renewal.
  name: reuse_key
  type: boolean
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-key-properties-schema.json
slug: azure-key-vault-data-plane-key-properties
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: KeyProperties
---
