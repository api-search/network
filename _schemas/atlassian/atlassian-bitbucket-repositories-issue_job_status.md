---
description: The status of an import or export job
layout: schema
name: issue_job_status
properties_list:
- description: ''
  name: type
  type: string
- description: The status of the import/export job
  name: status
  type: string
- description: The phase of the import/export job
  name: phase
  type: string
- description: The total number of issues being imported/exported
  name: total
  type: integer
- description: The total number of issues already imported/exported
  name: count
  type: integer
- description: The percentage of issues already imported/exported
  name: pct
  type: number
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-bitbucket-repositories-issue_job_status-schema.json
slug: atlassian-bitbucket-repositories-issue_job_status
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: issue_job_status
---
