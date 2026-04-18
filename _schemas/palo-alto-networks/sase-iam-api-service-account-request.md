---
description: ServiceAccountRequest schema from Palo Alto Networks SASE IAM Service API
layout: schema
name: ServiceAccountRequest
properties_list:
- description: Unique name for the service account within the TSG.
  name: name
  type: string
- description: Human-readable display name.
  name: display_name
  type: string
- description: Description of the service account's purpose.
  name: description
  type: string
- description: Tenant Service Group ID to create this service account in.
  name: tsg_id
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-iam-api-service-account-request-schema.json
slug: sase-iam-api-service-account-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ServiceAccountRequest
---
