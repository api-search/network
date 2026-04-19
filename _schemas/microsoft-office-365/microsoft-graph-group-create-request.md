---
description: ''
layout: schema
name: GroupCreateRequest
properties_list:
- description: The display name for the group.
  name: displayName
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: mailEnabled
  type: boolean
- description: ''
  name: mailNickname
  type: string
- description: ''
  name: securityEnabled
  type: boolean
- description: Set to ["Unified"] to create a Microsoft 365 group.
  name: groupTypes
  type: array
- description: ''
  name: visibility
  type: string
- description: URLs of user objects to set as owners at creation time.
  name: owners@odata.bind
  type: array
- description: URLs of user objects to set as members at creation time.
  name: members@odata.bind
  type: array
provider_name: Microsoft Office 365
provider_slug: microsoft-office-365
schema_file: json-schema/microsoft-graph-group-create-request-schema.json
slug: microsoft-graph-group-create-request
tags:
- Cloud
- Collaboration
- Enterprise
- Microsoft
- Productivity
title: GroupCreateRequest
---
