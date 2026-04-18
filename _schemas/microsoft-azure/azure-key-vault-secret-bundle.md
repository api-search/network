---
description: A secret consisting of a value, id, and attributes.
layout: schema
name: SecretBundle
properties_list:
- description: The secret value.
  name: value
  type: string
- description: The secret identifier.
  name: id
  type: string
- description: The content type of the secret.
  name: contentType
  type: string
- description: Application-specific metadata.
  name: tags
  type: object
- description: If the secret is backing a KV certificate, then this field specifies the corresponding key backing the certificate.
  name: kid
  type: string
- description: Whether the secret's lifetime is managed by Key Vault.
  name: managed
  type: boolean
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-key-vault-secret-bundle-schema.json
slug: azure-key-vault-secret-bundle
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: SecretBundle
---
