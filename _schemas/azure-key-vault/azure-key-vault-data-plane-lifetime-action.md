---
description: Action and its trigger that will be performed by Key Vault over the lifetime of a certificate.
layout: schema
name: LifetimeAction
properties_list:
- description: The condition that will execute the action.
  name: trigger
  type: object
- description: The action that will be executed.
  name: action
  type: object
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-lifetime-action-schema.json
slug: azure-key-vault-data-plane-lifetime-action
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: LifetimeAction
---
