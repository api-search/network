---
description: Contains information about a user account for an Amazon Connect instance.
layout: schema
name: User
properties_list:
- description: The identifier of the user account.
  name: Id
  type: string
- description: The Amazon Resource Name (ARN) of the user account.
  name: Arn
  type: string
- description: The user name assigned to the user account.
  name: Username
  type: string
- description: ''
  name: IdentityInfo
  type: object
- description: ''
  name: PhoneConfig
  type: object
- description: The identifier of the user account in the directory service that Amazon Connect uses to authenticate users.
  name: DirectoryUserId
  type: string
- description: The identifiers of the security profiles for the user.
  name: SecurityProfileIds
  type: array
- description: The identifier of the routing profile for the user.
  name: RoutingProfileId
  type: string
- description: The identifier of the hierarchy group for the user.
  name: HierarchyGroupId
  type: string
- description: The tags.
  name: Tags
  type: object
provider_name: Amazon Connect
provider_slug: amazon-connect
schema_file: json-schema/user-schema.json
slug: user
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
title: User
---
