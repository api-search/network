---
description: An IIO context representing a local or remote IIO system
layout: schema
name: IIOContext
properties_list:
- description: Context name (e.g., local, ip, usb)
  name: name
  type: string
- description: Context description
  name: description
  type: string
- description: IIO XML version
  name: xml_version
  type: string
- description: IIO devices in this context
  name: devices
  type: array
- description: Context-level attributes
  name: attrs
  type: object
provider_name: Analog Devices
provider_slug: analog-devices
schema_file: json-schema/analog-devices-iio-context-schema.json
slug: analog-devices-iio-context
tags:
- Embedded Systems
- Hardware
- IoT
- Semiconductor
- Signal Processing
title: IIOContext
---
