---
description: ScanIntegration schema from Palo Alto Networks Prisma Cloud Code Security API
layout: schema
name: ScanIntegration
properties_list:
- description: Unique integration identifier.
  name: id
  type: string
- description: Integration name.
  name: name
  type: string
- description: CI/CD platform type.
  name: type
  type: string
- description: Repository this integration is associated with.
  name: repositoryId
  type: string
- description: Whether the integration is active.
  name: enabled
  type: boolean
- description: ''
  name: createdAt
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-code-security-api-scan-integration-schema.json
slug: prisma-cloud-code-security-api-scan-integration
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ScanIntegration
---
