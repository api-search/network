---
description: The attributes of a key.
layout: schema
name: KeyAttributes
properties_list:
- description: Whether the key is enabled.
  name: enabled
  type: boolean
- description: Not before date in UTC (Unix time).
  name: nbf
  type: integer
- description: Expiry date in UTC (Unix time).
  name: exp
  type: integer
- description: Creation time in UTC (Unix time).
  name: created
  type: integer
- description: Last updated time in UTC (Unix time).
  name: updated
  type: integer
- description: The recovery level currently in effect.
  name: recoveryLevel
  type: string
- description: The soft-delete data retention days.
  name: recoverableDays
  type: integer
- description: Whether the private key can be exported.
  name: exportable
  type: boolean
- description: The underlying HSM platform.
  name: hsmPlatform
  type: string
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-key-vault-key-attributes-schema.json
slug: azure-key-vault-key-attributes
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: KeyAttributes
---
