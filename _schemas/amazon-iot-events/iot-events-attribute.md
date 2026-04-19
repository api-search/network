---
description: The attributes from the JSON payload that are made available by the input. Inputs are derived from messages sent to the AWS IoT Events system using <code>BatchPutMessage</code>. Each such message contains a JSON payload. Those attributes (and their paired values) specified here are available for use in the <code>condition</code> expressions used by detectors.
layout: schema
name: Attribute
properties_list:
- description: ''
  name: jsonPath
  type: object
provider_name: Amazon IoT Events
provider_slug: amazon-iot-events
schema_file: json-schema/iot-events-attribute-schema.json
slug: iot-events-attribute
tags:
- AWS
- Event Detection
- IoT
- State Machine
- Automation
title: Attribute
---
