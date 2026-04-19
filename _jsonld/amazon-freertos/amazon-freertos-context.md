---
class_count: 5
classes:
- SoftwareConfiguration
- OtaUpdate
- Device
- OtaFile
- Tag
context_file: json-ld/amazon-freertos-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-freertos/refs/heads/main/json-ld/amazon-freertos-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Freertos from Amazon FreeRTOS.
layout: jsonld
name: Amazon Freertos Context
namespaces:
- prefix: freertos
  uri: https://aws.amazon.com/freertos/vocabulary/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: softwareConfigurationId
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: hardwarePlatform
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: otaUpdateId
  type: string
- container: ''
  name: targets
  type: ''
- container: ''
  name: otaUpdateStatus
  type: string
- container: ''
  name: thingName
  type: string
- container: ''
  name: creationDate
  type: dateTime
- container: ''
  name: lastModifiedDate
  type: dateTime
property_count: 11
provider_name: Amazon FreeRTOS
provider_slug: amazon-freertos
slug: amazon-freertos-context
tags:
- AWS
- Embedded Systems
- IoT
- Microcontrollers
- RTOS
- JSON-LD
- Linked Data
- Semantic Web
---
