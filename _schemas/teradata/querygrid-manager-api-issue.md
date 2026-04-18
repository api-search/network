---
description: An issue detected in the QueryGrid environment.
layout: schema
name: Issue
properties_list:
- description: Unique issue identifier.
  name: id
  type: string
- description: Issue severity level.
  name: severity
  type: string
- description: Issue description message.
  name: message
  type: string
- description: Source component of the issue.
  name: source
  type: string
- description: Time when the issue was detected.
  name: timestamp
  type: string
provider_name: Teradata
provider_slug: teradata
schema_file: json-schema/querygrid-manager-api-issue-schema.json
slug: querygrid-manager-api-issue
tags:
- Analytics
- Cloud
- Data Management
- Data Warehousing
- Database
- Enterprise
- Machine Learning
- SQL
title: Issue
---
