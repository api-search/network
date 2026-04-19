---
description: Represents a file attached to an item in a vault.
layout: schema
name: File
properties_list:
- description: The unique identifier for the file.
  name: id
  type: string
- description: The name of the file.
  name: name
  type: string
- description: The size of the file in bytes.
  name: size
  type: integer
- description: The API path to retrieve the file content.
  name: content_path
  type: string
- description: ''
  name: section
  type: object
- description: The base64-encoded file content, included when inline_files is true.
  name: content
  type: string
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-connect-file-schema.json
slug: 1password-connect-file
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: File
---
