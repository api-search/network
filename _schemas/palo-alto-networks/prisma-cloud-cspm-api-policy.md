---
description: Policy schema from Palo Alto Networks Prisma Cloud CSPM API
layout: schema
name: Policy
properties_list:
- description: Unique policy identifier.
  name: policyId
  type: string
- description: Policy name.
  name: name
  type: string
- description: Type of policy check.
  name: policyType
  type: string
- description: Policy severity level.
  name: severity
  type: string
- description: Policy description.
  name: description
  type: string
- description: Recommended remediation for policy violations.
  name: recommendation
  type: string
- description: Cloud provider the policy applies to.
  name: cloudType
  type: string
- description: Whether the policy is active.
  name: enabled
  type: boolean
- description: Whether this is a built-in policy.
  name: systemDefault
  type: boolean
- description: ''
  name: rule
  type: object
- description: ''
  name: complianceMetadata
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-cspm-api-policy-schema.json
slug: prisma-cloud-cspm-api-policy
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Policy
---
