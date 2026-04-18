---
description: Represents a sharing permission on a drive item.
layout: schema
name: Permission
properties_list:
- description: The unique identifier of the permission.
  name: id
  type: string
- description: The type of permission (read, write, owner).
  name: roles
  type: array
- description: ''
  name: link
  type: object
- description: ''
  name: grantedTo
  type: object
provider_name: Microsoft Word
provider_slug: microsoft-word
schema_file: json-schema/graph-api-permission-schema.json
slug: graph-api-permission
tags:
- Documents
- Microsoft 365
- Office
- Productivity
- Word Processing
title: Permission
---
