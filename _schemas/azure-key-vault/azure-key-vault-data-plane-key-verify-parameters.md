---
description: The key verify parameters.
layout: schema
name: KeyVerifyParameters
properties_list:
- description: The signing/verification algorithm identifier.
  name: alg
  type: string
- description: The digest used for signing.
  name: digest
  type: string
- description: The signature to verify.
  name: value
  type: string
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-key-verify-parameters-schema.json
slug: azure-key-vault-data-plane-key-verify-parameters
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: KeyVerifyParameters
---
