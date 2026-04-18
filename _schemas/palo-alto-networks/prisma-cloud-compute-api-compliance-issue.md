---
description: ComplianceIssue schema from Palo Alto Networks Prisma Cloud Compute API
layout: schema
name: ComplianceIssue
properties_list:
- description: Compliance check ID.
  name: id
  type: integer
- description: Title of the compliance check.
  name: title
  type: string
- description: Severity of the compliance issue.
  name: severity
  type: string
- description: Explanation of why the resource failed the check.
  name: cause
  type: string
- description: Detailed description of the compliance requirement.
  name: description
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-compute-api-compliance-issue-schema.json
slug: prisma-cloud-compute-api-compliance-issue
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ComplianceIssue
---
