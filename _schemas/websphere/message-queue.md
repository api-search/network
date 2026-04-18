---
description: Represents an IBM MQ message queue including its configuration, runtime status, depth, and messaging properties for point-to-point and publish-subscribe messaging patterns.
layout: schema
name: IBM MQ Message Queue
properties_list:
- description: The unique name of the queue within the queue manager.
  name: name
  type: string
- description: Human-readable display name for the queue.
  name: displayName
  type: string
- description: Description of the queue purpose.
  name: description
  type: string
- description: Queue type.
  name: type
  type: string
- description: Name of the queue manager that owns this queue.
  name: queueManager
  type: string
- description: Maximum number of messages that can be held on the queue.
  name: maxDepth
  type: integer
- description: Maximum length of a message in bytes.
  name: maxMessageLength
  type: integer
- description: Current number of messages on the queue.
  name: currentDepth
  type: integer
- description: Message persistence configuration.
  name: persistence
  type: object
- description: Whether put operations are inhibited on this queue.
  name: inhibitPut
  type: boolean
- description: Whether get operations are inhibited on this queue.
  name: inhibitGet
  type: boolean
- description: Triggering configuration for the queue.
  name: triggerControl
  type: object
- description: Cluster queue properties (for cluster queues).
  name: cluster
  type: object
- description: Name of the dead letter queue for undeliverable messages.
  name: deadLetterQueue
  type: string
- description: Number of times a message can be backed out before being moved to the backout queue.
  name: backoutThreshold
  type: integer
- description: Name of the backout requeue queue.
  name: backoutQueue
  type: string
- description: Whether the queue can be opened for input by multiple applications.
  name: shareability
  type: string
- description: Default input open option.
  name: defaultInputOpenOption
  type: string
- description: Message priority settings.
  name: messagePriority
  type: object
- description: Runtime status information.
  name: status
  type: object
- description: Alias queue properties (for alias queues).
  name: alias
  type: object
- description: Remote queue properties (for remote queues).
  name: remote
  type: object
- description: Date and time the queue was created.
  name: createdDate
  type: string
- description: Date and time the queue was last modified.
  name: lastModified
  type: string
- description: Additional metadata associated with the queue.
  name: metadata
  type: object
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/message-queue.json
slug: message-queue
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: IBM MQ Message Queue
---
