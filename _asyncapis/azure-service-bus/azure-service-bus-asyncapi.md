---
channels:
- description: A Service Bus queue provides FIFO message delivery to one or more competing consumers. Messages are stored durably in the queue until retrieved by a receiver.
  name: '{queueName}'
  operation: publish
  operation_id: sendToQueue
  summary: Send a message to a queue
- description: A Service Bus topic enables publish-subscribe messaging. Publishers send messages to a topic, and subscribers receive messages from subscriptions associated with the topic.
  name: '{topicName}'
  operation: publish
  operation_id: sendToTopic
  summary: Publish a message to a topic
- description: A subscription to a Service Bus topic. Each subscription receives a copy of messages published to the topic, filtered by subscription rules.
  name: '{topicName}/subscriptions/{subscriptionName}'
  operation: subscribe
  operation_id: receiveFromSubscription
  summary: Receive a message from a topic subscription
description: Azure Service Bus is a fully managed enterprise message broker with message queues and publish-subscribe topics. This AsyncAPI spec describes the messaging patterns for sending and receiving messages via Service Bus queues and topics.
layout: asyncapi
messages:
- description: ''
  name: ServiceBusMessage
  summary: A message sent or received via Azure Service Bus.
  title: Service Bus Message
- description: ''
  name: DeadLetterMessage
  summary: A message moved to the dead-letter queue.
  title: Dead Letter Message
name: Azure Service Bus Messaging
provider_name: Azure Service Bus
provider_slug: azure-service-bus
servers:
- description: Azure Service Bus AMQP endpoint
  name: azure-service-bus
  protocol: amqp
  url: '{namespaceName}.servicebus.windows.net'
- description: Azure Service Bus HTTP endpoint
  name: azure-service-bus-https
  protocol: https
  url: '{namespaceName}.servicebus.windows.net'
slug: azure-service-bus-asyncapi
spec_file: asyncapi/azure-service-bus-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/azure-service-bus/refs/heads/main/asyncapi/azure-service-bus-asyncapi.yml
tags:
- Azure
- Cloud
- Enterprise
- Message Broker
- Messaging
- Pub/Sub
- Queues
- AsyncAPI
- Webhooks
- Events
version: '2021-11-01'
---
