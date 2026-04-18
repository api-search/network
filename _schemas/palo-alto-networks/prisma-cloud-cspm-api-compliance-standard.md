---
description: ComplianceStandard schema from Palo Alto Networks Prisma Cloud CSPM API
layout: schema
name: ComplianceStandard
properties_list:
- description: Unique compliance standard identifier.
  name: id
  type: string
- description: Name of the compliance standard.
  name: name
  type: string
- description: Standard description.
  name: description
  type: string
- description: Cloud providers the standard applies to.
  name: cloudType
  type: array
- description: Whether this is a built-in compliance standard.
  name: systemDefault
  type: boolean
- description: Number of policies mapped to this standard.
  name: policiesAssigned
  type: integer
- description: User who created the standard.
  name: createdBy
  type: string
- description: Epoch timestamp of last modification.
  name: lastModifiedTs
  type: integer
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-cspm-api-compliance-standard-schema.json
slug: prisma-cloud-cspm-api-compliance-standard
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ComplianceStandard
---
