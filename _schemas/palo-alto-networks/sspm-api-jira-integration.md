---
description: JiraIntegration schema from Palo Alto Networks SaaS Security Posture Management API
layout: schema
name: JiraIntegration
properties_list:
- description: Unique identifier of the Jira integration.
  name: id
  type: string
- description: Display name for the integration.
  name: name
  type: string
- description: Base URL of the Jira server or cloud instance.
  name: jira_url
  type: string
- description: Jira project key where tickets are created.
  name: project_key
  type: string
- description: Jira issue type for created tickets (e.g., Bug, Task).
  name: issue_type
  type: string
- description: Whether the integration is actively creating tickets.
  name: enabled
  type: boolean
- description: ''
  name: created_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sspm-api-jira-integration-schema.json
slug: sspm-api-jira-integration
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: JiraIntegration
---
