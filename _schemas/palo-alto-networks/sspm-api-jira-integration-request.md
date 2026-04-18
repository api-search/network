---
description: JiraIntegrationRequest schema from Palo Alto Networks SaaS Security Posture Management API
layout: schema
name: JiraIntegrationRequest
properties_list:
- description: Display name for this integration.
  name: name
  type: string
- description: Base URL of the Jira server or cloud instance.
  name: jira_url
  type: string
- description: Jira project key where tickets will be created.
  name: project_key
  type: string
- description: Jira issue type (e.g., Bug, Task, Story).
  name: issue_type
  type: string
- description: Jira API token for authentication.
  name: api_token
  type: string
- description: Email address associated with the Jira API token.
  name: email
  type: string
- description: Mapping from SSPM severity levels to Jira priorities.
  name: severity_mapping
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sspm-api-jira-integration-request-schema.json
slug: sspm-api-jira-integration-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: JiraIntegrationRequest
---
