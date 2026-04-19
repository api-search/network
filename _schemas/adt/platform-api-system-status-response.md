---
description: Response to an arm or disarm command.
layout: schema
name: SystemStatusResponse
properties_list:
- description: ID of the system.
  name: systemId
  type: string
- description: New system status after command.
  name: status
  type: string
- description: Timestamp of the status change.
  name: timestamp
  type: string
provider_name: ADT
provider_slug: adt
schema_file: json-schema/platform-api-system-status-response-schema.json
slug: platform-api-system-status-response
tags:
- Access Control
- Automation
- Home Security
- IoT
- Monitoring
- Security
- Smart Home
title: SystemStatusResponse
---
