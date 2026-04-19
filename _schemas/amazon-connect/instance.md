---
description: The Amazon Connect instance.
layout: schema
name: Instance
properties_list:
- description: The identifier of the Amazon Connect instance.
  name: Id
  type: string
- description: The Amazon Resource Name (ARN) of the instance.
  name: Arn
  type: string
- description: The identity management type.
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
provider_name: Amazon Connect
provider_slug: amazon-connect
schema_file: json-schema/instance-schema.json
slug: instance
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
title: Instance
---
