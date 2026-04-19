---
description: The key operation result.
layout: schema
name: KeyOperationResult
properties_list:
- description: Key identifier.
  name: kid
  type: string
- description: The result of the operation.
  name: value
  type: string
- description: Initialization vector for symmetric algorithms.
  name: iv
  type: string
- description: Authentication tag for authenticated encryption algorithms.
  name: tag
  type: string
- description: Additional authenticated data.
  name: aad
  type: string
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-key-operation-result-schema.json
slug: azure-key-vault-data-plane-key-operation-result
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: KeyOperationResult
---
