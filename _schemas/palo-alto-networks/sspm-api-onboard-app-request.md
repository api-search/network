---
description: OnboardAppRequest schema from Palo Alto Networks SaaS Security Posture Management API
layout: schema
name: OnboardAppRequest
properties_list:
- description: Application type to onboard (e.g., google_workspace, microsoft_365, salesforce).
  name: app_type
  type: string
- description: Optional display name for this application instance.
  name: display_name
  type: string
- description: Authentication credentials required to connect to the application.
  name: credentials
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sspm-api-onboard-app-request-schema.json
slug: sspm-api-onboard-app-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: OnboardAppRequest
---
