---
description: Schema for an Amazon Connect instance resource, representing a cloud contact center instance with users, queues, and contact flows.
layout: schema
name: Amazon Connect Instance
properties_list:
- description: The identifier of the Amazon Connect instance.
  name: Id
  type: string
- description: The ARN of the Amazon Connect instance.
  name: Arn
  type: string
- description: The identity management type of the instance.
  name: IdentityManagementType
  type: string
- description: The alias of the instance.
  name: InstanceAlias
  type: string
- description: When the instance was created.
  name: CreatedTime
  type: string
- description: The service role of the instance.
  name: ServiceRole
  type: string
- description: The state of the instance.
  name: InstanceStatus
  type: string
- description: Whether inbound calls are enabled.
  name: InboundCallsEnabled
  type: boolean
- description: Whether outbound calls are enabled.
  name: OutboundCallsEnabled
  type: boolean
- description: ''
  name: User
  type: object
- description: ''
  name: Queue
  type: object
provider_name: Amazon Connect
provider_slug: amazon-connect
schema_file: json-schema/amazon-connect-instance-schema.json
slug: amazon-connect-instance
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
title: Amazon Connect Instance
---
