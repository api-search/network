---
description: Represents a Dynatrace environment (tenant) associated with the account.
layout: schema
name: Environment
properties_list:
- description: The unique environment identifier (tenant ID).
  name: id
  type: string
- description: The display name of the environment.
  name: name
  type: string
- description: The current status of the environment.
  name: status
  type: string
- description: Whether the environment is a trial environment.
  name: trial
  type: boolean
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/dynatrace-account-management-environment-schema.json
slug: dynatrace-account-management-environment
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
title: Environment
---
