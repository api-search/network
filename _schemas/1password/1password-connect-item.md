---
description: Represents a summary of a 1Password item with basic metadata. Use the get item endpoint to retrieve full details.
layout: schema
name: Item
properties_list:
- description: The unique identifier for the item.
  name: id
  type: string
- description: The title of the item.
  name: title
  type: string
- description: ''
  name: vault
  type: object
- description: The category of the item.
  name: category
  type: string
- description: URLs associated with the item.
  name: urls
  type: array
- description: Whether the item is marked as a favorite.
  name: favorite
  type: boolean
- description: Tags applied to the item.
  name: tags
  type: array
- description: The version number of the item.
  name: version
  type: integer
- description: The state of the item.
  name: state
  type: string
- description: The date and time the item was created.
  name: createdAt
  type: string
- description: The date and time the item was last updated.
  name: updatedAt
  type: string
- description: The UUID of the user who last edited the item.
  name: lastEditedBy
  type: string
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-connect-item-schema.json
slug: 1password-connect-item
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: Item
---
