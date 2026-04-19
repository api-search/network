---
description: CreateUserRequest schema from Amazon Connect Service API
layout: schema
name: CreateUserRequest
properties_list:
- description: The user name for the account.
  name: Username
  type: string
- description: The password for the user account.
  name: Password
  type: string
- description: ''
  name: IdentityInfo
  type: object
- description: ''
  name: PhoneConfig
  type: object
- description: ''
  name: DirectoryUserId
  type: string
- description: The identifier of the security profile for the user.
  name: SecurityProfileIds
  type: array
- description: The identifier of the routing profile for the user.
  name: RoutingProfileId
  type: string
- description: ''
  name: HierarchyGroupId
  type: string
- description: ''
  name: Tags
  type: object
provider_name: Amazon Connect
provider_slug: amazon-connect
schema_file: json-schema/create-user-request-schema.json
slug: create-user-request
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
title: CreateUserRequest
---
