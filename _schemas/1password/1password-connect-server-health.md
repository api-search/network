---
description: Represents the health status of the Connect server and its dependencies.
layout: schema
name: ServerHealth
properties_list:
- description: The name of the Connect server.
  name: name
  type: string
- description: The version of the Connect server.
  name: version
  type: string
- description: The health status of server dependencies.
  name: dependencies
  type: array
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-connect-server-health-schema.json
slug: 1password-connect-server-health
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: ServerHealth
---
