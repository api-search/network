---
description: The result returned after closing a problem.
layout: schema
name: ProblemCloseResult
properties_list:
- description: The ID of the closed problem.
  name: problemId
  type: string
- description: Whether the problem is in the process of closing. The problem may take a short time to fully transition to RESOLVED status.
  name: closing
  type: boolean
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/problems-api-v2-problem-close-result-schema.json
slug: problems-api-v2-problem-close-result
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
title: ProblemCloseResult
---
