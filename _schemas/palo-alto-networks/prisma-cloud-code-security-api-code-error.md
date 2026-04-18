---
description: CodeError schema from Palo Alto Networks Prisma Cloud Code Security API
layout: schema
name: CodeError
properties_list:
- description: Unique error identifier.
  name: errorId
  type: string
- description: Checkov policy ID that triggered the error (e.g., CKV_AWS_18).
  name: policyId
  type: string
- description: Human-readable name of the violated policy.
  name: policyName
  type: string
- description: Error severity level.
  name: severity
  type: string
- description: Error category based on the type of scan that detected it.
  name: category
  type: string
- description: Current status of the error.
  name: status
  type: string
- description: Name of the IaC resource where the error was detected.
  name: resourceName
  type: string
- description: Type of the IaC resource.
  name: resourceType
  type: string
- description: Relative path to the file containing the error.
  name: filePath
  type: string
- description: Start and end line numbers of the affected code block.
  name: fileLineRange
  type: array
- description: Repository where the error was found.
  name: repositoryId
  type: string
- description: Branch where the error was detected.
  name: branch
  type: string
- description: URL to documentation explaining the policy and remediation steps.
  name: guideline
  type: string
- description: Timestamp when the error was first detected.
  name: firstDetected
  type: string
- description: Timestamp of the most recent scan where the error was found.
  name: lastDetected
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-code-security-api-code-error-schema.json
slug: prisma-cloud-code-security-api-code-error
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: CodeError
---
