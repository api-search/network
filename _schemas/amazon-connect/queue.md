---
description: Contains information about a queue.
layout: schema
name: Queue
properties_list:
- description: The name of the queue.
  name: Name
  type: string
- description: The Amazon Resource Name (ARN) for the queue.
  name: QueueArn
  type: string
- description: The identifier for the queue.
  name: QueueId
  type: string
- description: The description of the queue.
  name: Description
  type: string
- description: ''
  name: OutboundCallerConfig
  type: object
- description: The identifier for the hours of operation.
  name: HoursOfOperationId
  type: string
- description: The maximum number of contacts that can be in the queue before it is considered full.
  name: MaxContacts
  type: integer
- description: The status of the queue.
  name: Status
  type: string
- description: ''
  name: Tags
  type: object
provider_name: Amazon Connect
provider_slug: amazon-connect
schema_file: json-schema/queue-schema.json
slug: queue
tags:
- AWS
- Chat
- Contact Center
- Customer Service
- Voice
- AI
- Omnichannel
title: Queue
---
