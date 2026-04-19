---
description: A FreeRTOS software configuration specifying firmware libraries, settings, and target hardware platform.
layout: schema
name: SoftwareConfiguration
properties_list:
- description: Unique ID of the software configuration.
  name: softwareConfigurationId
  type: string
- description: Name of the software configuration.
  name: name
  type: string
- description: Optional description.
  name: description
  type: string
- description: ARN of the software configuration.
  name: arn
  type: string
- description: Status of the configuration.
  name: status
  type: string
- description: Version string.
  name: version
  type: string
- description: Target microcontroller platform (e.g., ESP32, STM32).
  name: hardwarePlatform
  type: string
- description: ''
  name: creationDate
  type: string
- description: ''
  name: lastUpdatedDate
  type: string
provider_name: Amazon FreeRTOS
provider_slug: amazon-freertos
schema_file: json-schema/amazon-freertos-software-configuration-schema.json
slug: amazon-freertos-software-configuration
tags:
- AWS
- Embedded Systems
- IoT
- Microcontrollers
- RTOS
title: SoftwareConfiguration
---
