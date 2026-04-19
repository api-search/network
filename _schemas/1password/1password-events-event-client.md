---
description: Information about the client application used in an event.
layout: schema
name: EventClient
properties_list:
- description: The name of the 1Password application.
  name: app_name
  type: string
- description: The version of the application.
  name: app_version
  type: string
- description: The name of the operating system platform.
  name: platform_name
  type: string
- description: The version of the operating system.
  name: platform_version
  type: string
- description: The name of the operating system.
  name: os_name
  type: string
- description: The version of the operating system.
  name: os_version
  type: string
- description: The IP address of the client.
  name: ip
  type: string
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-events-event-client-schema.json
slug: 1password-events-event-client
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: EventClient
---
