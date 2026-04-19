---
description: An over-the-air firmware update job for FreeRTOS microcontroller devices.
layout: schema
name: OtaUpdate
properties_list:
- description: Unique OTA update identifier.
  name: otaUpdateId
  type: string
- description: ARN of the OTA update.
  name: otaUpdateArn
  type: string
- description: Current status of the OTA update.
  name: otaUpdateStatus
  type: string
- description: ''
  name: description
  type: string
- description: ARNs of target devices, things, or thing groups.
  name: targets
  type: array
- description: Delivery protocols (MQTT or HTTP).
  name: protocols
  type: array
- description: ''
  name: creationDate
  type: string
- description: ''
  name: lastModifiedDate
  type: string
- description: ''
  name: awsIotJobId
  type: string
- description: ''
  name: awsIotJobArn
  type: string
provider_name: Amazon FreeRTOS
provider_slug: amazon-freertos
schema_file: json-schema/amazon-freertos-ota-update-schema.json
slug: amazon-freertos-ota-update
tags:
- AWS
- Embedded Systems
- IoT
- Microcontrollers
- RTOS
title: OtaUpdate
---
