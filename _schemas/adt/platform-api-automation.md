---
description: An automation rule or smart home scene.
layout: schema
name: Automation
properties_list:
- description: Unique identifier of the automation.
  name: id
  type: string
- description: Display name of the automation.
  name: name
  type: string
- description: What triggers this automation.
  name: trigger
  type: string
- description: Whether the automation is currently active.
  name: enabled
  type: boolean
- description: List of actions performed by this automation.
  name: actions
  type: array
provider_name: ADT
provider_slug: adt
schema_file: json-schema/platform-api-automation-schema.json
slug: platform-api-automation
tags:
- Access Control
- Automation
- Home Security
- IoT
- Monitoring
- Security
- Smart Home
title: Automation
---
