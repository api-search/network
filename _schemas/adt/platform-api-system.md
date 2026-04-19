---
description: An ADT security system.
layout: schema
name: System
properties_list:
- description: Unique identifier of the system.
  name: id
  type: string
- description: Display name of the system.
  name: name
  type: string
- description: Current arming status.
  name: status
  type: string
- description: Physical address of the protected property.
  name: address
  type: string
- description: Type of security system.
  name: type
  type: string
- description: Timestamp of last status change.
  name: lastModified
  type: string
provider_name: ADT
provider_slug: adt
schema_file: json-schema/platform-api-system-schema.json
slug: platform-api-system
tags:
- Access Control
- Automation
- Home Security
- IoT
- Monitoring
- Security
- Smart Home
title: System
---
