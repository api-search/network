---
consumed_apis:
- amazon-sqs
description: Message queuing workflow for managing SQS queues, sending and receiving messages, batch operations, dead-letter queue management, and access control. Used by developers and DevOps engineers for microservices decoupling and asynchronous processing.
layout: capability
name: Amazon SQS Message Queuing
operations:
- description: List all SQS queues
  method: GET
  name: list-queues
  path: /v1/queues
- description: Create a new SQS queue
  method: POST
  name: create-queue
  path: /v1/queues
- description: Send a message to a queue
  method: POST
  name: send-message
  path: /v1/messages
- description: List dead-letter queue source queues
  method: GET
  name: list-dlq-sources
  path: /v1/dead-letter-queues
personas: []
provider_name: Amazon SQS
provider_slug: amazon-sqs
search_terms:
- create a new standard or fifo queue
- delete message
- set attributes for a queue
- list queue tags
- message operations
- send message
- delete a message from a queue
- list queues that feed a dead-letter queue
- list dead-letter queue source queues
- dead-letter queue management
- get queue attributes
- change the visibility timeout of a message
- list dead letter source queues
- add tags to a queue
- get queue url
- list tags for a queue
- create queue
- purge queue
- delete message batch
- list queues
- add a permission to a queue
- list all sqs queues
- delete up to 10 messages in a batch
- add permission
- send a message to a queue
- remove permission
- distributed systems
- delete queue
- queue management
- list dlq sources
- get attributes for a queue
- microservices
- aws
- amazon
- delete all messages in a queue
- messaging
- send up to 10 messages in a batch
- get the url of a queue by name
- create a new sqs queue
- send message batch
- remove a permission from a queue
- cloud
- receive message
- start message move task
- change message visibility
- delete an sqs queue
- queue
- tag queue
- start moving messages from a dead-letter queue
- receive messages from a queue
- set queue attributes
slug: message-queuing
tags:
- Amazon
- AWS
- Messaging
- Queue
tools:
- description: List all SQS queues
  hints:
    openWorld: true
    readOnly: true
  name: list-queues
- description: Create a new standard or FIFO queue
  hints:
    readOnly: false
  name: create-queue
- description: Delete an SQS queue
  hints:
    destructive: true
  name: delete-queue
- description: Get the URL of a queue by name
  hints:
    readOnly: true
  name: get-queue-url
- description: Get attributes for a queue
  hints:
    readOnly: true
  name: get-queue-attributes
- description: Set attributes for a queue
  hints:
    idempotent: true
    readOnly: false
  name: set-queue-attributes
- description: Delete all messages in a queue
  hints:
    destructive: true
  name: purge-queue
- description: Send a message to a queue
  hints:
    readOnly: false
  name: send-message
- description: Receive messages from a queue
  hints:
    readOnly: true
  name: receive-message
- description: Delete a message from a queue
  hints:
    destructive: true
  name: delete-message
- description: Send up to 10 messages in a batch
  hints:
    readOnly: false
  name: send-message-batch
- description: Delete up to 10 messages in a batch
  hints:
    destructive: true
  name: delete-message-batch
- description: Change the visibility timeout of a message
  hints:
    idempotent: true
    readOnly: false
  name: change-message-visibility
- description: List queues that feed a dead-letter queue
  hints:
    readOnly: true
  name: list-dead-letter-source-queues
- description: Start moving messages from a dead-letter queue
  hints:
    readOnly: false
  name: start-message-move-task
- description: List tags for a queue
  hints:
    readOnly: true
  name: list-queue-tags
- description: Add tags to a queue
  hints:
    readOnly: false
  name: tag-queue
- description: Add a permission to a queue
  hints:
    readOnly: false
  name: add-permission
- description: Remove a permission from a queue
  hints:
    destructive: true
  name: remove-permission
---
