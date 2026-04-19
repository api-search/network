---
description: The key operations parameters.
layout: schema
name: KeyOperationsParameters
properties_list:
- description: Algorithm identifier.
  name: alg
  type: string
- description: The value to operate on.
  name: value
  type: string
- description: Initialization vector for symmetric algorithms.
  name: iv
  type: string
- description: Additional data to authenticate but not encrypt/decrypt.
  name: aad
  type: string
- description: The tag to verify when performing decryption with an authenticated algorithm.
  name: tag
  type: string
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-key-operations-parameters-schema.json
slug: azure-key-vault-data-plane-key-operations-parameters
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: KeyOperationsParameters
---
