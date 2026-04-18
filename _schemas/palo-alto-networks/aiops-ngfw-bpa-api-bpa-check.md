---
description: BPACheck schema from Palo Alto Networks AIOps for NGFW BPA API
layout: schema
name: BPACheck
properties_list:
- description: Unique identifier of the check.
  name: check_id
  type: string
- description: Best practice category this check belongs to.
  name: category
  type: string
- description: Name of the best practice check.
  name: name
  type: string
- description: Description of what this check evaluates.
  name: description
  type: string
- description: Result status of this check.
  name: status
  type: string
- description: Severity if this check fails.
  name: severity
  type: string
- description: Current configuration value found on the device.
  name: current_value
  type: string
- description: Recommended configuration value per best practices.
  name: recommended_value
  type: string
- description: Step-by-step remediation guidance for failed checks.
  name: remediation
  type: string
- description: Reference URLs with additional guidance.
  name: references
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/aiops-ngfw-bpa-api-bpa-check-schema.json
slug: aiops-ngfw-bpa-api-bpa-check
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: BPACheck
---
