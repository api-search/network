---
description: DeviceTag schema from Palo Alto Networks IoT Security API
layout: schema
name: DeviceTag
properties_list:
- description: Unique tag identifier.
  name: id
  type: string
- description: Tag name.
  name: name
  type: string
- description: Tag description.
  name: description
  type: string
- description: Number of devices assigned this tag.
  name: device_count
  type: integer
- description: Timestamp when the tag was created.
  name: created_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/iot-security-api-device-tag-schema.json
slug: iot-security-api-device-tag
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: DeviceTag
---
