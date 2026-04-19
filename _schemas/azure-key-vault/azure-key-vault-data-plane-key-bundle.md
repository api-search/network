---
description: A KeyBundle consisting of a WebKey plus its attributes.
layout: schema
name: KeyBundle
properties_list:
- description: Application specific metadata in the form of key-value pairs.
  name: tags
  type: object
- description: True if the key's lifetime is managed by key vault. If this is a key backing a certificate, then managed will be true.
  name: managed
  type: boolean
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-key-bundle-schema.json
slug: azure-key-vault-data-plane-key-bundle
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: KeyBundle
---
