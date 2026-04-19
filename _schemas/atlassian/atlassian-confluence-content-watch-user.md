---
description: This essentially the same as the `User` object, but no `_links` property and no `_expandable` property (therefore, different required fields).
layout: schema
name: WatchUser
properties_list:
- description: ''
  name: type
  type: string
- description: ''
  name: displayName
  type: string
- description: ''
  name: timeZone
  type: string
- description: ''
  name: operations
  type: array
- description: ''
  name: isExternalCollaborator
  type: boolean
- description: ''
  name: accountType
  type: string
- description: ''
  name: email
  type: string
- description: ''
  name: publicName
  type: string
- description: ''
  name: personalSpace
  type: object
- description: ''
  name: externalCollaborator
  type: boolean
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-confluence-content-watch-user-schema.json
slug: atlassian-confluence-content-watch-user
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: WatchUser
---
