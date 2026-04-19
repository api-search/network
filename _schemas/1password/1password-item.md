---
description: Represents a complete 1Password item stored in a vault, including its fields, sections, URLs, tags, and associated metadata. Items are the primary unit of secret storage in 1Password.
layout: schema
name: 1Password Item
properties_list:
- description: The unique identifier for the item.
  name: id
  type: string
- description: The title of the item displayed in the 1Password interface.
  name: title
  type: string
- description: ''
  name: vault
  type: object
- description: The category that determines the item template and available fields.
  name: category
  type: string
- description: URLs associated with the item, such as website login pages.
  name: urls
  type: array
- description: Whether the item is marked as a favorite.
  name: favorite
  type: boolean
- description: Tags applied to the item for organization.
  name: tags
  type: array
- description: The version number of the item, incremented on each update.
  name: version
  type: integer
- description: The current state of the item.
  name: state
  type: string
- description: The fields of the item containing secrets and metadata values.
  name: fields
  type: array
- description: Sections used to organize fields into logical groups within the item.
  name: sections
  type: array
- description: The ISO 8601 date and time the item was created.
  name: createdAt
  type: string
- description: The ISO 8601 date and time the item was last updated.
  name: updatedAt
  type: string
- description: The UUID of the user who last edited the item.
  name: lastEditedBy
  type: string
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-item-schema.json
slug: 1password-item
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: 1Password Item
---
