---
description: A batch result error entry
layout: schema
name: BatchResultErrorEntry
properties_list:
- description: The Id of the entry that caused the error
  name: Id
  type: string
- description: An error code representing the type of error
  name: Code
  type: string
- description: A message explaining the error
  name: Message
  type: string
- description: Specifies whether the error happened due to the caller of the batch API action
  name: SenderFault
  type: boolean
provider_name: Amazon SQS
provider_slug: amazon-sqs
schema_file: json-schema/amazon-sqs-batch-result-error-entry-schema.json
slug: amazon-sqs-batch-result-error-entry
tags:
- AWS
- Cloud
- Distributed Systems
- Messaging
- Microservices
- Queue
title: BatchResultErrorEntry
---
