---
description: A schema defining the structure and variables of events analyzed by Amazon Fraud Detector.
layout: schema
name: EventType
properties_list:
- description: Name of the event type.
  name: name
  type: string
- description: ''
  name: description
  type: string
- description: Variables included in each event of this type.
  name: eventVariables
  type: array
- description: Fraud/legit classification labels for this event type.
  name: labels
  type: array
- description: Entity types (e.g., customer, account) involved in this event.
  name: entityTypes
  type: array
- description: ''
  name: eventIngestion
  type: string
- description: ''
  name: arn
  type: string
provider_name: Amazon Fraud Detector
provider_slug: amazon-fraud-detector
schema_file: json-schema/amazon-fraud-detector-event-type-schema.json
slug: amazon-fraud-detector-event-type
tags:
- AWS
- Financial Services
- Fraud Detection
- Machine Learning
- Security
title: EventType
---
