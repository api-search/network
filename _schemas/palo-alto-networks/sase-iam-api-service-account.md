---
description: ServiceAccount schema from Palo Alto Networks SASE IAM Service API
layout: schema
name: ServiceAccount
properties_list:
- description: Unique identifier of the service account.
  name: id
  type: string
- description: Unique name of the service account within the TSG.
  name: name
  type: string
- description: Human-readable display name.
  name: display_name
  type: string
- description: Description of the service account's purpose.
  name: description
  type: string
- description: Tenant Service Group ID this service account belongs to.
  name: tsg_id
  type: string
- description: Number of active credential keys for this service account.
  name: key_count
  type: integer
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-iam-api-service-account-schema.json
slug: sase-iam-api-service-account
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ServiceAccount
---
