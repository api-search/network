---
description: A data integration event
layout: schema
name: DataIntegrationEvent
properties_list:
- description: The instance identifier
  name: instanceId
  type: string
- description: The event identifier
  name: eventId
  type: string
- description: The event type
  name: eventType
  type: string
- description: The event group identifier
  name: eventGroupId
  type: string
- description: The event timestamp
  name: eventTimestamp
  type: string
- description: The event data payload
  name: data
  type: string
provider_name: Amazon Supply Chain
provider_slug: amazon-supply-chain
schema_file: json-schema/amazon-supply-chain-data-integration-event-schema.json
slug: amazon-supply-chain-data-integration-event
tags:
- AWS
- ERP Integration
- Logistics
- Machine Learning
- Supply Chain
title: DataIntegrationEvent
---
