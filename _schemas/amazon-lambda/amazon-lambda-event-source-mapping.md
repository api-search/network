---
description: A Lambda event source mapping that connects an event source to a Lambda function.
layout: schema
name: EventSourceMapping
properties_list:
- description: The identifier of the event source mapping.
  name: UUID
  type: string
- description: The ARN of the event source.
  name: EventSourceArn
  type: string
- description: The ARN of the Lambda function.
  name: FunctionArn
  type: string
- description: The state of the event source mapping.
  name: State
  type: string
- description: The maximum number of records in each batch.
  name: BatchSize
  type: integer
provider_name: Amazon Lambda
provider_slug: amazon-lambda
schema_file: json-schema/amazon-lambda-event-source-mapping-schema.json
slug: amazon-lambda-event-source-mapping
tags:
- AWS
- Compute
- Event-Driven
- FaaS
- Functions
- Serverless
title: EventSourceMapping
---
