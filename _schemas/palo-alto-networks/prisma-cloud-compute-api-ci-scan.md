---
description: CIScan schema from Palo Alto Networks Prisma Cloud Compute API
layout: schema
name: CIScan
properties_list:
- description: ''
  name: entityInfo
  type: object
- description: Whether the scan passed the configured policy thresholds.
  name: pass
  type: boolean
- description: ''
  name: vulnerabilitiesCount
  type: integer
- description: ''
  name: complianceIssuesCount
  type: integer
- description: ''
  name: vulnerabilityDistribution
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-compute-api-ci-scan-schema.json
slug: prisma-cloud-compute-api-ci-scan
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: CIScan
---
