---
description: Represents a record of an item in a shared vault being accessed, modified, or used.
layout: schema
name: ItemUsage
properties_list:
- description: The unique identifier for the item usage record.
  name: uuid
  type: string
- description: When the item was accessed.
  name: timestamp
  type: string
- description: The version of the item that was used.
  name: used_version
  type: integer
- description: The UUID of the vault containing the item.
  name: vault_uuid
  type: string
- description: The UUID of the item that was used.
  name: item_uuid
  type: string
- description: The type of action performed on the item.
  name: action
  type: string
- description: ''
  name: user
  type: object
- description: ''
  name: client
  type: object
- description: ''
  name: location
  type: object
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-events-item-usage-schema.json
slug: 1password-events-item-usage
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: ItemUsage
---
