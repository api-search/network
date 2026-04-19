---
description: An Amazon SQS message
layout: schema
name: Message
properties_list:
- description: A unique identifier for the message
  name: MessageId
  type: string
- description: An identifier associated with the act of receiving the message. A new receipt handle is returned every time you receive a message. When deleting a message, you provide the last received receipt handle
  name: ReceiptHandle
  type: string
- description: An MD5 digest of the non-URL-encoded message body string
  name: MD5OfBody
  type: string
- description: The message's contents (not URL-encoded)
  name: Body
  type: string
- description: A map of the attributes requested in ReceiveMessage to their respective values.
  name: Attribute
  type: array
- description: Each message attribute consists of a Name, Type, and Value.
  name: MessageAttribute
  type: array
provider_name: Amazon SQS
provider_slug: amazon-sqs
schema_file: json-schema/amazon-sqs-message-schema.json
slug: amazon-sqs-message
tags:
- AWS
- Cloud
- Distributed Systems
- Messaging
- Microservices
- Queue
title: Message
---
