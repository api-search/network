---
description: The secret set parameters.
layout: schema
name: SecretSetParameters
properties_list:
- description: The value of the secret.
  name: value
  type: string
- description: Application-specific metadata.
  name: tags
  type: object
- description: Type of the secret value such as a password.
  name: contentType
  type: string
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-key-vault-secret-set-parameters-schema.json
slug: azure-key-vault-secret-set-parameters
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: SecretSetParameters
---
