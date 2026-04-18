---
description: Host schema from Palo Alto Networks Prisma Cloud Compute API
layout: schema
name: Host
properties_list:
- description: Unique host identifier.
  name: _id
  type: string
- description: Host machine hostname.
  name: hostname
  type: string
- description: Timestamp of the most recent host scan.
  name: scanTime
  type: string
- description: Operating system distribution.
  name: osDistro
  type: string
- description: Operating system version.
  name: osDistroVersion
  type: string
- description: Linux kernel version.
  name: kernelVersion
  type: string
- description: Cloud provider metadata for the host.
  name: cloudMetadata
  type: object
- description: Vulnerabilities discovered on the host.
  name: vulnerabilities
  type: array
- description: Total number of vulnerabilities found.
  name: vulnerabilitiesCount
  type: integer
- description: ''
  name: vulnerabilityDistribution
  type: object
- description: ''
  name: complianceIssues
  type: array
- description: ''
  name: complianceIssuesCount
  type: integer
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-compute-api-host-schema.json
slug: prisma-cloud-compute-api-host
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Host
---
