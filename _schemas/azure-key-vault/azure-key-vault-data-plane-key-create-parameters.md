---
description: The key create parameters.
layout: schema
name: KeyCreateParameters
properties_list:
- description: 'The key size in bits. For example: 2048, 3072, or 4096 for RSA.'
  name: key_size
  type: integer
- description: The public exponent for a RSA key.
  name: public_exponent
  type: integer
- description: JSON web key operations.
  name: key_ops
  type: array
- description: Application specific metadata in the form of key-value pairs.
  name: tags
  type: object
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-key-create-parameters-schema.json
slug: azure-key-vault-data-plane-key-create-parameters
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: KeyCreateParameters
---
