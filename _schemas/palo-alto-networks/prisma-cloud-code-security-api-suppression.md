---
description: Suppression schema from Palo Alto Networks Prisma Cloud Code Security API
layout: schema
name: Suppression
properties_list:
- description: Unique suppression rule identifier.
  name: suppressionId
  type: string
- description: Checkov policy ID being suppressed.
  name: policyId
  type: string
- description: Human-readable policy name.
  name: policyName
  type: string
- description: Scope of the suppression.
  name: suppressionType
  type: string
- description: Reason provided for the suppression.
  name: justification
  type: string
- description: Email address of the user who created the suppression.
  name: createdBy
  type: string
- description: Timestamp when the suppression was created.
  name: createdAt
  type: string
- description: Expiration date. Null if the suppression does not expire.
  name: expirationDate
  type: string
- description: Number of errors currently suppressed by this rule.
  name: suppressedErrorCount
  type: integer
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-code-security-api-suppression-schema.json
slug: prisma-cloud-code-security-api-suppression
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Suppression
---
