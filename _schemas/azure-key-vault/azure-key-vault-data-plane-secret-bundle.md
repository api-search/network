---
description: A secret consisting of a value, id and its attributes.
layout: schema
name: SecretBundle
properties_list:
- description: The secret value.
  name: value
  type: string
- description: The secret id.
  name: id
  type: string
- description: The content type of the secret.
  name: contentType
  type: string
- description: Application specific metadata in the form of key-value pairs.
  name: tags
  type: object
- description: If this is a secret backing a KV certificate, then this field specifies the corresponding key backing the KV certificate.
  name: kid
  type: string
- description: True if the secret's lifetime is managed by key vault. If this is a secret backing a certificate, then managed will be true.
  name: managed
  type: boolean
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-secret-bundle-schema.json
slug: azure-key-vault-data-plane-secret-bundle
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: SecretBundle
---
