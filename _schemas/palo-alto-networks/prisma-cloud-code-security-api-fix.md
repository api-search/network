---
description: Fix schema from Palo Alto Networks Prisma Cloud Code Security API
layout: schema
name: Fix
properties_list:
- description: Unique fix suggestion identifier.
  name: fixId
  type: string
- description: Checkov policy ID associated with the fix.
  name: policyId
  type: string
- description: Human-readable policy name.
  name: policyName
  type: string
- description: Severity of the original finding.
  name: severity
  type: string
- description: IaC resource name where the fix applies.
  name: resourceName
  type: string
- description: Relative path to the file requiring the fix.
  name: filePath
  type: string
- description: Start and end line numbers of the code to be replaced.
  name: lineRange
  type: array
- description: Original code snippet that contains the misconfiguration.
  name: originalCode
  type: string
- description: Suggested replacement code that resolves the misconfiguration.
  name: suggestedCode
  type: string
- description: IaC framework of the affected file.
  name: framework
  type: string
- description: Repository where the fix applies.
  name: repositoryId
  type: string
- description: Branch where the fix applies.
  name: branch
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-code-security-api-fix-schema.json
slug: prisma-cloud-code-security-api-fix
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Fix
---
