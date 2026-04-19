---
description: A FreeRTOS-capable microcontroller device registered in AWS IoT.
layout: schema
name: Device
properties_list:
- description: IoT thing name for the device.
  name: thingName
  type: string
- description: ARN of the IoT thing.
  name: thingArn
  type: string
- description: Type classification of the device.
  name: thingTypeName
  type: string
- description: Device attributes (hardware model, firmware version, etc.)
  name: attributes
  type: object
- description: Thing record version.
  name: version
  type: integer
provider_name: Amazon FreeRTOS
provider_slug: amazon-freertos
schema_file: json-schema/amazon-freertos-device-schema.json
slug: amazon-freertos-device
tags:
- AWS
- Embedded Systems
- IoT
- Microcontrollers
- RTOS
title: Device
---
