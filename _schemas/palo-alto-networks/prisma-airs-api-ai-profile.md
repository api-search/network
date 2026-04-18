---
description: AIProfile schema from Palo Alto Networks Prisma AIRS API
layout: schema
name: AIProfile
properties_list:
- description: Unique identifier of the profile.
  name: profile_id
  type: string
- description: Profile name used to reference this profile in scan requests.
  name: profile_name
  type: string
- description: Human-readable description of the profile purpose and use case.
  name: description
  type: string
- description: Detection categories configured in this profile.
  name: detection_categories
  type: array
- description: Timestamp when the profile was created.
  name: created_at
  type: string
- description: Timestamp of the most recent profile modification.
  name: updated_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-airs-api-ai-profile-schema.json
slug: prisma-airs-api-ai-profile
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AIProfile
---
