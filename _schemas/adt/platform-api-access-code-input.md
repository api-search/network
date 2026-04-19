---
description: Request to create an access code.
layout: schema
name: AccessCodeInput
properties_list:
- description: Display name for the access code.
  name: name
  type: string
- description: The numeric access code (4-8 digits).
  name: code
  type: string
- description: Type of access code.
  name: type
  type: string
- description: Expiration time for temporary codes.
  name: expiresAt
  type: string
provider_name: ADT
provider_slug: adt
schema_file: json-schema/platform-api-access-code-input-schema.json
slug: platform-api-access-code-input
tags:
- Access Control
- Automation
- Home Security
- IoT
- Monitoring
- Security
- Smart Home
title: AccessCodeInput
---
