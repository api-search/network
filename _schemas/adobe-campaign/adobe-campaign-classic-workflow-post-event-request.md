---
description: SOAP envelope containing a signal event to post to a workflow, including the workflow ID, signal activity name, and optional XML variables.
layout: schema
name: WorkflowPostEventRequest
properties_list:
- description: Internal ID of the target workflow.
  name: workflowId
  type: integer
- description: Name of the external signal activity in the workflow.
  name: activity
  type: string
- description: XML element containing variable parameters to pass to the workflow transition.
  name: variables
  type: object
provider_name: Adobe Campaign
provider_slug: adobe-campaign
schema_file: json-schema/adobe-campaign-classic-workflow-post-event-request-schema.json
slug: adobe-campaign-classic-workflow-post-event-request
tags:
- Campaign Management
- Customer Experience
- Email Marketing
- Marketing Automation
- Multi-Channel Marketing
title: WorkflowPostEventRequest
---
