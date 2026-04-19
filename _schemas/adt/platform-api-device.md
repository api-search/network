---
description: A security device (sensor, camera, lock, or smart home device).
layout: schema
name: Device
properties_list:
- description: Unique identifier of the device.
  name: id
  type: string
- description: Display name of the device.
  name: name
  type: string
- description: Type of device.
  name: type
  type: string
- description: Current status of the device.
  name: status
  type: string
- description: Security zone the device belongs to.
  name: zone
  type: string
- description: Battery level percentage (0-100) for battery-powered devices.
  name: batteryLevel
  type: integer
- description: Timestamp of last device activity.
  name: lastActivity
  type: string
provider_name: ADT
provider_slug: adt
schema_file: json-schema/platform-api-device-schema.json
slug: platform-api-device
tags:
- Access Control
- Automation
- Home Security
- IoT
- Monitoring
- Security
- Smart Home
title: Device
---
