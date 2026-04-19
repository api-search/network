---
class_count: 5
classes:
- IIODevice
- IIOChannel
- IIOContext
- name
- description
context_file: json-ld/analog-devices-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/analog-devices/refs/heads/main/json-ld/analog-devices-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Analog Devices from Analog Devices.
layout: jsonld
name: Analog Devices Context
namespaces:
- prefix: adi
  uri: https://www.analog.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: string
- container: ''
  name: label
  type: string
- container: set
  name: channels
  type: ''
- container: ''
  name: attrs
  type: reference
- container: ''
  name: scanElement
  type: boolean
- container: set
  name: devices
  type: ''
property_count: 6
provider_name: Analog Devices
provider_slug: analog-devices
slug: analog-devices-context
tags:
- Embedded Systems
- Hardware
- IoT
- Semiconductor
- Signal Processing
- JSON-LD
- Linked Data
- Semantic Web
---
