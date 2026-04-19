---
description: ''
layout: schema
name: User
properties_list:
- description: ''
  name: type
  type: string
- description: The account type of the user, may return empty string if unavailable. App is if the user is a bot user created on behalf of an Atlassian app.
  name: accountType
  type: string
- description: The email address of the user. Depending on the user's privacy setting, this may return an empty string.
  name: email
  type: string
- description: The public name or nickname of the user. Will always contain a value.
  name: publicName
  type: string
- description: The displays name of the user. Depending on the user's privacy setting, this may be the same as publicName.
  name: displayName
  type: string
- description: This displays user time zone. Depending on the user's privacy setting, this may return null.
  name: timeZone
  type: string
- description: Whether the user is an external collaborator user
  name: isExternalCollaborator
  type: boolean
- description: Whether the user is an external collaborator user
  name: externalCollaborator
  type: boolean
- description: ''
  name: operations
  type: array
- description: ''
  name: _expandable
  type: object
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-confluence-content-user-schema.json
slug: atlassian-confluence-content-user
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: User
---
