---
description: OnboardingStatus schema from Palo Alto Networks SASE Configuration Orchestration API
layout: schema
name: OnboardingStatus
properties_list:
- description: Remote network identifier.
  name: id
  type: string
- description: Current onboarding phase.
  name: status
  type: string
- description: Individual onboarding steps and their completion state.
  name: steps
  type: array
- description: Error description if onboarding failed.
  name: error_message
  type: string
- description: ''
  name: started_at
  type: string
- description: ''
  name: completed_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-config-orchestration-api-onboarding-status-schema.json
slug: sase-config-orchestration-api-onboarding-status
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: OnboardingStatus
---
