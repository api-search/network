---
description: ManagedDevice schema from Palo Alto Networks Prisma Access Browser Management API
layout: schema
name: ManagedDevice
properties_list:
- description: Unique identifier of the managed device.
  name: device_id
  type: string
- description: Device hostname.
  name: hostname
  type: string
- description: Operating system platform.
  name: platform
  type: string
- description: Installed Prisma Access Browser version.
  name: browser_version
  type: string
- description: Device compliance status.
  name: compliance_status
  type: string
- description: ID of the last user who logged in on this device.
  name: user_id
  type: string
- description: Timestamp of the device's last check-in.
  name: last_seen_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-access-browser-api-managed-device-schema.json
slug: prisma-access-browser-api-managed-device
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ManagedDevice
---
