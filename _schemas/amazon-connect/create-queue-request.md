---
description: CreateQueueRequest schema from Amazon Connect Service API
layout: schema
name: CreateQueueRequest
properties_list:
- description: The name of the queue.
  name: Name
  type: string
- description: The description of the queue.
  name: Description
  type: string
- description: The identifier for the hours of operation.
  name: HoursOfOperationId
  type: string
- description: The maximum number of contacts that can be in the queue.
  name: MaxContacts
  type: integer
- description: ''
  name: OutboundCallerConfig
  type: object
- description: ''
  name: Tags
  type: object
provider_name: Amazon Connect
provider_slug: amazon-connect
schema_file: json-schema/create-queue-request-schema.json
slug: create-queue-request
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
title: CreateQueueRequest
---
