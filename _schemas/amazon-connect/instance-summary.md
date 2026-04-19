---
description: Information about the Amazon Connect instance.
layout: schema
name: InstanceSummary
properties_list:
- description: The identifier of the instance.
  name: Id
  type: string
- description: The ARN of the instance.
  name: Arn
  type: string
- description: The identity management type.
  name: IdentityManagementType
  type: string
- description: The alias of the instance.
  name: InstanceAlias
  type: string
- description: The state of the instance.
  name: InstanceStatus
  type: string
- description: ''
  name: InboundCallsEnabled
  type: boolean
- description: ''
  name: OutboundCallsEnabled
  type: boolean
provider_name: Amazon Connect
provider_slug: amazon-connect
schema_file: json-schema/instance-summary-schema.json
slug: instance-summary
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
title: InstanceSummary
---
