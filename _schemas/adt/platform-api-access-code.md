---
description: An access code for a security system.
layout: schema
name: AccessCode
properties_list:
- description: Unique identifier of the access code.
  name: id
  type: string
- description: Display name for the access code.
  name: name
  type: string
- description: Type of access code.
  name: type
  type: string
- description: Expiration timestamp for temporary codes.
  name: expiresAt
  type: string
- description: List of permissions granted by this code.
  name: permissions
  type: array
provider_name: ADT
provider_slug: adt
schema_file: json-schema/platform-api-access-code-schema.json
slug: platform-api-access-code
tags:
- Access Control
- Automation
- Home Security
- IoT
- Monitoring
- Security
- Smart Home
title: AccessCode
---
