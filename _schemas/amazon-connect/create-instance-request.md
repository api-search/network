---
description: CreateInstanceRequest schema from Amazon Connect Service API
layout: schema
name: CreateInstanceRequest
properties_list:
- description: The idempotency token.
  name: ClientToken
  type: string
- description: The type of identity management for your Amazon Connect users.
  name: IdentityManagementType
  type: string
- description: The name for your instance.
  name: InstanceAlias
  type: string
- description: The identifier for the directory.
  name: DirectoryId
  type: string
- description: Your contact center handles incoming contacts.
  name: InboundCallsEnabled
  type: boolean
- description: Your contact center allows outbound calls.
  name: OutboundCallsEnabled
  type: boolean
- description: The tags used to organize, track, or control access for this resource.
  name: Tags
  type: object
provider_name: Amazon Connect
provider_slug: amazon-connect
schema_file: json-schema/create-instance-request-schema.json
slug: create-instance-request
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
title: CreateInstanceRequest
---
