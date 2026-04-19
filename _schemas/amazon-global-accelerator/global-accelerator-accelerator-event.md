---
description: A complex type that contains a <code>Timestamp</code> value and <code>Message</code> for changes that you make to an accelerator in Global Accelerator. Messages stored here provide progress or error information when you update an accelerator from IPv4 to dual-stack, or from dual-stack to IPv4. Global Accelerator stores a maximum of ten event messages.
layout: schema
name: AcceleratorEvent
properties_list:
- description: ''
  name: Message
  type: object
- description: ''
  name: Timestamp
  type: object
provider_name: Amazon Global Accelerator
provider_slug: amazon-global-accelerator
schema_file: json-schema/global-accelerator-accelerator-event-schema.json
slug: global-accelerator-accelerator-event
tags:
- Availability
- AWS
- CDN
- Global
- Load Balancing
- Networking
- Performance
title: AcceleratorEvent
---
