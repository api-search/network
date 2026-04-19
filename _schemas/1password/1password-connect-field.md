---
description: Represents a field within an item that stores a value such as a username, password, or other data.
layout: schema
name: Field
properties_list:
- description: The unique identifier for the field.
  name: id
  type: string
- description: ''
  name: section
  type: object
- description: The type of the field.
  name: type
  type: string
- description: The purpose of the field, indicating its role within the item.
  name: purpose
  type: string
- description: The human-readable label for the field.
  name: label
  type: string
- description: The value stored in the field.
  name: value
  type: string
- description: Whether the field value should be auto-generated.
  name: generate
  type: boolean
- description: The entropy (strength) of the generated value.
  name: entropy
  type: number
- description: ''
  name: recipe
  type: object
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-connect-field-schema.json
slug: 1password-connect-field
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: Field
---
