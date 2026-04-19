---
description: Representation of a Linux IIO device as exposed by libiio
layout: schema
name: IIODevice
properties_list:
- description: Device name
  name: name
  type: string
- description: Device identifier
  name: id
  type: string
- description: Optional device label
  name: label
  type: string
- description: List of IIO channels
  name: channels
  type: array
- description: Device-level attributes
  name: attrs
  type: object
provider_name: Analog Devices
provider_slug: analog-devices
schema_file: json-schema/analog-devices-iio-device-schema.json
slug: analog-devices-iio-device
tags:
- Embedded Systems
- Hardware
- IoT
- Semiconductor
- Signal Processing
title: IIODevice
---
