---
description: Repository schema from Palo Alto Networks Prisma Cloud Code Security API
layout: schema
name: Repository
properties_list:
- description: Unique repository identifier in Prisma Cloud.
  name: id
  type: string
- description: Repository name.
  name: name
  type: string
- description: Repository owner or organization name.
  name: owner
  type: string
- description: Full repository name in owner/repo format.
  name: fullName
  type: string
- description: VCS provider type.
  name: sourceType
  type: string
- description: Default branch of the repository.
  name: defaultBranch
  type: string
- description: URL to the repository in the VCS provider.
  name: url
  type: string
- description: Whether the repository is publicly accessible.
  name: isPublic
  type: boolean
- description: Timestamp of the most recent scan.
  name: lastScanDate
  type: string
- description: Status of the most recent scan.
  name: lastScanStatus
  type: string
- description: Count of open errors by severity.
  name: errorCounts
  type: object
- description: Timestamp when the repository was connected.
  name: createdAt
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-code-security-api-repository-schema.json
slug: prisma-cloud-code-security-api-repository
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Repository
---
