---
description: Report schema from Palo Alto Networks Prisma Cloud CSPM API
layout: schema
name: Report
properties_list:
- description: Unique report identifier.
  name: id
  type: string
- description: Report name.
  name: name
  type: string
- description: Report type.
  name: type
  type: string
- description: Current report generation status.
  name: status
  type: string
- description: Epoch timestamp when the report was created.
  name: createdOn
  type: integer
- description: Epoch timestamp of last modification.
  name: lastModifiedOn
  type: integer
- description: URL for downloading the completed report.
  name: downloadUrl
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-cspm-api-report-schema.json
slug: prisma-cloud-cspm-api-report
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Report
---
