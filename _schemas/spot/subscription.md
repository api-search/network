---
description: A Spot subscription defines an event notification configuration, delivering alerts about Spot resource events to a specified endpoint via a chosen protocol.
layout: schema
name: Spot Subscription
properties_list:
- description: The unique identifier of the subscription.
  name: id
  type: string
- description: The identifier of the resource to monitor.
  name: resourceId
  type: string
- description: The protocol used to deliver event notifications.
  name: protocol
  type: string
- description: The endpoint URL or address where notifications are sent.
  name: endpoint
  type: string
- description: The type of event to subscribe to.
  name: eventType
  type: string
- description: Custom formatting options for the event notification payload.
  name: eventFormat
  type: object
provider_name: Spot
provider_slug: spot
schema_file: json-schema/subscription.json
slug: subscription
tags:
- Autoscaling
- Cloud Infrastructure
- Containers
- Cost Optimization
- FinOps
- Kubernetes
- Spot Instances
title: Spot Subscription
---
