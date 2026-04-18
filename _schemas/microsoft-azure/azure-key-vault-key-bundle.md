---
description: A key bundle containing the key and its attributes.
layout: schema
name: KeyBundle
properties_list:
- description: Application-specific metadata in the form of key-value pairs.
  name: tags
  type: object
- description: Whether the key's lifetime is managed by Key Vault.
  name: managed
  type: boolean
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-key-vault-key-bundle-schema.json
slug: azure-key-vault-key-bundle
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: KeyBundle
---
