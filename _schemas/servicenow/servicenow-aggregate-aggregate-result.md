---
description: The aggregate statistics result. Structure varies based on the requested aggregate types and group-by fields.
layout: schema
name: AggregateResult
properties_list:
- description: Contains the computed aggregate values organized by field name and aggregate type.
  name: stats
  type: object
- description: When group-by fields are specified, contains an entry for each unique group with its aggregate values.
  name: group_by
  type: array
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-aggregate-aggregate-result-schema.json
slug: servicenow-aggregate-aggregate-result
tags:
- Automation
- Cloud Services
- Digital Workflows
- Enterprise Platform
- IT Service Management
- ITSM
- Processes
- T1
- Workflow Automation
- Workflows
title: AggregateResult
---
