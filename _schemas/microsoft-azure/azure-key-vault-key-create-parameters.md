---
description: The key create parameters.
layout: schema
name: KeyCreateParameters
properties_list:
- description: The type of key to create.
  name: kty
  type: string
- description: The key size in bits. For example, 2048, 3072, or 4096 for RSA.
  name: key_size
  type: integer
- description: JSON web key operations.
  name: key_ops
  type: array
- description: Application-specific metadata.
  name: tags
  type: object
- description: Elliptic curve name (for EC key types).
  name: crv
  type: string
- description: Whether the private key can be exported.
  name: exportable
  type: boolean
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-key-vault-key-create-parameters-schema.json
slug: azure-key-vault-key-create-parameters
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: KeyCreateParameters
---
