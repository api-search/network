---
description: DSPMPolicy schema from Palo Alto Networks Prisma Cloud DSPM API
layout: schema
name: DSPMPolicy
properties_list:
- description: Unique DSPM policy identifier.
  name: id
  type: string
- description: Policy name.
  name: name
  type: string
- description: Policy description.
  name: description
  type: string
- description: Whether the policy is currently active.
  name: enabled
  type: boolean
- description: Severity level of violations detected by this policy.
  name: severity
  type: string
- description: Classification label this policy governs.
  name: classification
  type: string
- description: Security controls required for data matching this policy.
  name: requiredControls
  type: array
- description: Cloud providers this policy applies to.
  name: cloudProviders
  type: array
- description: ''
  name: createdAt
  type: string
- description: ''
  name: updatedAt
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-dspm-api-dspm-policy-schema.json
slug: prisma-cloud-dspm-api-dspm-policy
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: DSPMPolicy
---
