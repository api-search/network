---
description: Unit of work sent to an activity worker.
layout: schema
name: ActivityTask
properties_list:
- description: ''
  name: taskToken
  type: object
- description: ''
  name: activityId
  type: object
- description: ''
  name: startedEventId
  type: object
- description: ''
  name: workflowExecution
  type: object
- description: ''
  name: activityType
  type: object
- description: ''
  name: input
  type: object
provider_name: Amazon Simple Workflow Service
provider_slug: amazon-swf
schema_file: json-schema/amazon-swf-activitytask-schema.json
slug: amazon-swf-activitytask
tags:
- Automation
- AWS
- Task Coordination
- Workflow
title: ActivityTask
---
