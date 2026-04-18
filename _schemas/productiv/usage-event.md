---
description: Represents a usage event for an application, capturing user actions such as starting a video call, sending messages, or uploading files.
layout: schema
name: UsageEvent
properties_list:
- description: The timestamp of the event in milliseconds since epoch.
  name: timestamp
  type: integer
- description: The email address of the user who performed the action.
  name: email
  type: string
- description: The name of the action or activity performed.
  name: eventName
  type: string
provider_name: Productiv
provider_slug: productiv
schema_file: json-schema/usage-event.json
slug: usage-event
tags:
- Application Portfolio
- Provisioning
- SaaS Management
- Spend Management
- Usage Analytics
title: UsageEvent
---
