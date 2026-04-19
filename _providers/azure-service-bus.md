---
api_count: 1
apis:
- description: 'Azure Service Bus is a fully managed enterprise message broker supporting message queues and publish-subscribe topics with features like dead-lettering, sessions, scheduled delivery, and transactions '
  name: Azure Service Bus
  slug: azure-service-bus
asyncapis:
- description: 'Azure Service Bus is a fully managed enterprise message broker with message queues and publish-subscribe topics. This AsyncAPI spec describes the messaging patterns for sending and receiving messages '
  name: Azure Service Bus Messaging
  slug: azure-service-bus-asyncapi
capabilities:
- description: Unified workflow for managing Azure Service Bus messaging infrastructure including namespaces, queues, topics, and subscriptions. Designed for cloud architects and platform engineers managing enterpri
  name: Azure Service Bus Messaging Management
  slug: messaging-management
common:
- title: ''
  type: Portal
  url: https://azure.microsoft.com/en-us/products/service-bus
- title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/service-bus-messaging/
- title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quickstart-portal
- title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/service-bus/
- title: ''
  type: GitHubRepository
  url: https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/servicebus
- title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
created: '2026-03-26'
description: Azure Service Bus is a fully managed enterprise message broker with message queues and publish-subscribe topics, providing reliable message delivery for decoupling applications and services in cloud and hybrid environments.
features:
- description: Point-to-point messaging with FIFO delivery, sessions, dead-lettering, and duplicate detection for reliable asynchronous communication.
  name: Message Queues
- description: One-to-many messaging with topic subscriptions, filters, and actions for event-driven architectures.
  name: Publish-Subscribe Topics
- description: Automatic routing of undeliverable or failed messages to a secondary queue for inspection and reprocessing.
  name: Dead-Letter Queue
- description: Schedule messages for future delivery at a specified time without requiring sender availability.
  name: Scheduled Delivery
- description: ACID transaction support for grouping multiple operations across queues and topics into atomic units.
  name: Transactions
- description: Automatically forward messages from one queue or subscription to another entity for chaining processing stages.
  name: Auto-Forwarding
image: /assets/icons/azure-service-bus.png
integrations:
- description: Trigger serverless functions automatically when messages arrive in queues or topic subscriptions.
  name: Azure Functions
- description: Build automated workflows that send and receive Service Bus messages with no-code connectors.
  name: Azure Logic Apps
- description: Route Service Bus events to other Azure services for real-time event processing and monitoring.
  name: Azure Event Grid
jsonld:
- class_count: 0
  name: Azure Service Bus Context
  property_count: 0
  slug: azure-service-bus-context
layout: provider
modified: '2026-04-18'
name: Azure Service Bus
rules:
- name: Azure Service Bus API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: azure-service-bus-spectral-rules
skills: []
slug: azure-service-bus
solutions: []
tags:
- Azure
- Cloud
- Enterprise
- Message Broker
- Messaging
- Pub/Sub
- Queues
url: https://raw.githubusercontent.com/api-evangelist/azure-service-bus/refs/heads/main/apis.yml
use_cases:
- description: Decouple microservices and distributed applications using asynchronous messaging for independent scaling and deployment.
  name: Application Decoupling
- description: Buffer incoming requests during traffic spikes to protect backend services from overload.
  name: Load Leveling
- description: Build event-driven systems using publish-subscribe topics to broadcast events to multiple subscribers.
  name: Event-Driven Architecture
- description: Coordinate multi-step business processes using message sessions and scheduled delivery for reliable workflow execution.
  name: Workflow Orchestration
---
