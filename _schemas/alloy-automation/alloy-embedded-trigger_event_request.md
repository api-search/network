---
description: Request body for triggering a custom workflow event
layout: schema
name: TriggerEventRequest
properties_list:
- description: Identifier of the user triggering the event
  name: userId
  type: string
- description: Event name to trigger
  name: event
  type: string
- description: Event payload data
  name: data
  type: object
provider_name: Alloy Automation
provider_slug: alloy-automation
schema_file: json-schema/alloy-embedded-trigger_event_request-schema.json
slug: alloy-embedded-trigger_event_request
tags:
- Automation
- Embedded Integrations
- Integrations
- iPaaS
- Unified API
- Workflows
title: TriggerEventRequest
---
