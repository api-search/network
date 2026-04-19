---
description: A firmware file included in a FreeRTOS OTA update job.
layout: schema
name: OtaFile
properties_list:
- description: Name of the OTA file on the device.
  name: fileName
  type: string
- description: Version of the firmware file.
  name: fileVersion
  type: string
- description: S3 or Stream location of the firmware binary.
  name: fileLocation
  type: object
- description: Code signing configuration for the firmware file.
  name: codeSigning
  type: object
- description: User-defined file type (0-255).
  name: fileType
  type: integer
provider_name: Amazon FreeRTOS
provider_slug: amazon-freertos
schema_file: json-schema/amazon-freertos-ota-file-schema.json
slug: amazon-freertos-ota-file
tags:
- AWS
- Embedded Systems
- IoT
- Microcontrollers
- RTOS
title: OtaFile
---
