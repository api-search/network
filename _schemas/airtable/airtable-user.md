---
description: An Airtable user account within an enterprise organization. Users have identity attributes, management states, and permission levels across workspaces and bases.
layout: schema
name: Airtable User
properties_list:
- description: The unique identifier for the user (starts with 'usr').
  name: id
  type: string
- description: The email address of the user.
  name: email
  type: string
- description: The display name of the user.
  name: name
  type: string
- description: The management state of the user within the enterprise.
  name: state
  type: string
- description: Whether the user has enterprise administrator privileges.
  name: isAdmin
  type: boolean
- description: The time when the user account was created.
  name: createdTime
  type: string
- description: The time of the user's most recent activity. Null if the user has never been active.
  name: lastActivityTime
  type:
  - string
  - 'null'
- description: The user's collaboration details across workspaces, bases, and interfaces.
  name: collaborations
  type: object
provider_name: Airtable
provider_slug: airtable
schema_file: json-schema/airtable-user-schema.json
slug: airtable-user
tags:
- Applications
- Collaboration
- Data
- Databases
- Low-Code
- Productivity
- Spreadsheets
title: Airtable User
---
