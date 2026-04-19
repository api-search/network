---
description: An AWS Control Tower landing zone.
layout: schema
name: LandingZone
properties_list:
- description: The ARN of the landing zone.
  name: arn
  type: string
- description: The drift status of the landing zone.
  name: driftStatus
  type: object
- description: The latest available version of the landing zone.
  name: latestAvailableVersion
  type: string
- description: The landing zone manifest document.
  name: manifest
  type: object
- description: The landing zone deployment status.
  name: status
  type: string
- description: The current deployed version of the landing zone.
  name: version
  type: string
provider_name: Amazon Control Tower
provider_slug: amazon-control-tower
schema_file: json-schema/landing-zone-schema.json
slug: landing-zone
tags:
- AWS
- Compliance
- Governance
- Landing Zone
- Multi-Account
- Security
- Controls
title: LandingZone
---
