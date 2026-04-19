---
description: 'Used to filter the workflow executions in visibility APIs by various time-based rules. Each parameter, if specified, defines a rule that must be satisfied by each returned query result. The parameter values are in the <a href="https://en.wikipedia.org/wiki/Unix_time">Unix Time format</a>. For example: <code>"oldestDate": 1325376070.</code>'
layout: schema
name: ExecutionTimeFilter
properties_list:
- description: ''
  name: oldestDate
  type: object
- description: ''
  name: latestDate
  type: object
provider_name: Amazon Simple Workflow Service
provider_slug: amazon-swf
schema_file: json-schema/amazon-swf-executiontimefilter-schema.json
slug: amazon-swf-executiontimefilter
tags:
- Automation
- AWS
- Task Coordination
- Workflow
title: ExecutionTimeFilter
---
