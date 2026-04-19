---
channels:
- description: A standard Amazon SQS queue. Standard queues offer maximum throughput, best-effort ordering, and at-least-once delivery. Messages can be received out of the order in which they were sent, and a message might be delivered more than once.
  name: standardQueue
- description: A FIFO (First-In-First-Out) Amazon SQS queue. FIFO queues are designed to guarantee that messages are processed exactly once, in the exact order that they are sent. FIFO queue names must end with the .fifo suffix.
  name: fifoQueue
- description: A dead-letter queue (DLQ) that receives messages that could not be processed successfully from their source queue. Messages are moved to the DLQ after the maximum number of receive attempts (maxReceiveCount) has been exceeded. DLQs help isolate and debug problematic messages.
  name: deadLetterQueue
- description: An AWS Lambda event source mapping for Amazon SQS. Lambda polls the SQS queue and invokes your Lambda function synchronously with an event that contains queue messages. Lambda reads messages in batches and invokes the function once for each batch. The event source mapping reads messages from the queue, constructs a batch, and invokes the function. For standard queues, Lambda uses long polling to poll the queue until it becomes active. For FIFO queues, Lambda sends messages to the function in the order that it receives them.
  name: lambdaEventSource
description: AsyncAPI specification for Amazon SQS event-driven messaging patterns. Amazon SQS provides reliable, highly-scalable hosted queues for storing messages as they travel between applications or microservices. SQS supports both standard queues (maximum throughput, best-effort ordering, at-least-once delivery) and FIFO queues (exactly-once processing, in order). This specification describes the asynchronous messaging channels and message formats used when integrating with SQS, including AWS Lambda event source mappings that automatically poll SQS queues and invoke Lambda functions with batches of messages.
layout: asyncapi
messages:
- description: An SQS message that can be sent to or received from a standard queue. Messages can contain up to 256 KiB of text data including XML, JSON, and unformatted text. Custom message attributes can be attached for additional metadata.
  name: sqsMessage
  summary: A message in an Amazon SQS standard queue
  title: SQS Standard Queue Message
- description: An SQS FIFO message that guarantees exactly-once processing and ordered delivery within a message group. FIFO messages require a MessageGroupId and either a MessageDeduplicationId or content-based deduplication must be enabled on the queue.
  name: sqsFifoMessage
  summary: A message in an Amazon SQS FIFO queue
  title: SQS FIFO Queue Message
- description: A collection of up to 10 messages to be sent to an SQS queue in a single batch request. The total payload size of all messages combined must not exceed 256 KiB.
  name: sqsBatchMessage
  summary: A batch of up to 10 messages for an SQS queue
  title: SQS Batch Message
- description: A message that was moved to a dead-letter queue after exceeding the maximum receive count on its source queue. The message retains its original body and attributes, along with system attributes indicating how many times it was received and when it was first received.
  name: sqsDeadLetterMessage
  summary: A message in an SQS dead-letter queue
  title: SQS Dead-Letter Queue Message
- description: 'When Lambda polls an SQS queue and finds messages, it constructs a batch and invokes the function synchronously with this event payload. The event contains an array of SQS message records, each with the message body, attributes, and metadata. For standard queues, Lambda may invoke the function with '
  name: lambdaSqsEvent
  summary: The event payload sent to AWS Lambda from an SQS event source mapping
  title: Lambda SQS Event
name: Amazon Simple Queue Service (SQS) Event Source Mapping
provider_name: Amazon SQS
provider_slug: amazon-sqs
servers:
- description: Amazon SQS Regional Endpoint
  name: production
  protocol: https
  url: ''
slug: amazon-sqs-asyncapi
spec_file: asyncapi/amazon-sqs-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/amazon-sqs/refs/heads/main/asyncapi/amazon-sqs-asyncapi.yml
tags:
- AWS
- Cloud
- Distributed Systems
- Messaging
- Microservices
- Queue
- AsyncAPI
- Webhooks
- Events
version: '2012-11-05'
---
