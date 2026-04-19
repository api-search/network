---
consumed_apis:
- service-bus
description: Unified workflow for managing Azure Service Bus messaging infrastructure including namespaces, queues, topics, and subscriptions. Designed for cloud architects and platform engineers managing enterprise messaging.
layout: capability
name: Azure Service Bus Messaging Management
operations:
- description: List all namespaces
  method: GET
  name: list-namespaces
  path: /v1/namespaces
- description: Get namespace details
  method: GET
  name: get-namespace
  path: /v1/namespaces/{namespaceName}
- description: List queues
  method: GET
  name: list-queues
  path: /v1/queues
- description: List topics
  method: GET
  name: list-topics
  path: /v1/topics
personas: []
provider_name: Azure Service Bus
provider_slug: azure-service-bus
search_terms:
- azure
- list queues within a service bus namespace
- list all namespaces
- list namespaces
- namespace details
- pub/sub
- cloud infrastructure
- delete a service bus namespace
- create or update a service bus namespace
- delete namespace
- service bus
- message queues
- message broker
- list topics within a service bus namespace
- list queues
- get namespace
- service bus namespaces
- get namespace details
- messaging
- cloud
- get details of a specific service bus namespace
- list topics
- create or update namespace
- pub/sub topics
- enterprise
- queues
- list azure service bus namespaces in a subscription
slug: messaging-management
tags:
- Azure
- Service Bus
- Messaging
- Cloud Infrastructure
tools:
- description: List Azure Service Bus namespaces in a subscription
  hints:
    openWorld: true
    readOnly: true
  name: list-namespaces
- description: Get details of a specific Service Bus namespace
  hints:
    readOnly: true
  name: get-namespace
- description: Create or update a Service Bus namespace
  hints:
    idempotent: true
    readOnly: false
  name: create-or-update-namespace
- description: Delete a Service Bus namespace
  hints:
    destructive: true
    idempotent: true
  name: delete-namespace
- description: List queues within a Service Bus namespace
  hints:
    readOnly: true
  name: list-queues
- description: List topics within a Service Bus namespace
  hints:
    readOnly: true
  name: list-topics
---
