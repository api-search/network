---
description: PostureCheck schema from Palo Alto Networks SaaS Security Posture Management API
layout: schema
name: PostureCheck
properties_list:
- description: Unique identifier of the posture check result.
  name: check_id
  type: string
- description: ID of the onboarded application this check applies to.
  name: app_id
  type: string
- description: Name of the security posture check.
  name: check_name
  type: string
- description: Category of the posture check.
  name: check_type
  type: string
- description: Severity level if the check fails.
  name: severity
  type: string
- description: Current result status of the check.
  name: status
  type: string
- description: Description of what the check evaluates.
  name: description
  type: string
- description: Step-by-step remediation guidance for failed checks.
  name: remediation
  type: string
- description: Compliance frameworks this check maps to (e.g., CIS, SOC2, ISO27001).
  name: compliance_frameworks
  type: array
- description: Timestamp when the check was last evaluated.
  name: last_evaluated_at
  type: string
- description: Justification text if the check is suppressed.
  name: suppression_justification
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sspm-api-posture-check-schema.json
slug: sspm-api-posture-check
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: PostureCheck
---
