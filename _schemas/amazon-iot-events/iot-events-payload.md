---
description: <p>Information needed to configure the payload.</p> <p>By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use <code>contentExpression</code>.</p>
layout: schema
name: Payload
properties_list:
- description: ''
  name: contentExpression
  type: object
- description: ''
  name: type
  type: object
provider_name: Amazon IoT Events
provider_slug: amazon-iot-events
schema_file: json-schema/iot-events-payload-schema.json
slug: iot-events-payload
tags:
- AWS
- Event Detection
- IoT
- State Machine
- Automation
title: Payload
---
