---
description: The policy rules under which the key can be exported.
layout: schema
name: KeyReleasePolicy
properties_list:
- description: Content type and version of key release policy.
  name: contentType
  type: string
- description: Blob encoding the policy rules under which the key can be released.
  name: data
  type: string
- description: Defines the mutability state of the policy. Once marked immutable, this flag cannot be reset and the policy cannot be changed under any circumstances.
  name: immutable
  type: boolean
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-key-release-policy-schema.json
slug: azure-key-vault-data-plane-key-release-policy
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: KeyReleasePolicy
---
