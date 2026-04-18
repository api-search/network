---
description: CloudAccount schema from Palo Alto Networks Prisma Cloud CSPM API
layout: schema
name: CloudAccount
properties_list:
- description: Cloud provider account identifier.
  name: accountId
  type: string
- description: Display name of the account.
  name: name
  type: string
- description: Cloud provider type.
  name: cloudType
  type: string
- description: Whether monitoring is enabled.
  name: enabled
  type: boolean
- description: Number of policies applied to this account.
  name: numberOfPolicies
  type: integer
- description: Epoch timestamp of last modification.
  name: lastModifiedTs
  type: integer
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-cspm-api-cloud-account-schema.json
slug: prisma-cloud-cspm-api-cloud-account
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: CloudAccount
---
