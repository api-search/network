---
description: An Amazon Fraud Detector ML model trained to score transactions for fraud risk.
layout: schema
name: Model
properties_list:
- description: Unique identifier for the model.
  name: modelId
  type: string
- description: The type of fraud detection model.
  name: modelType
  type: string
- description: ''
  name: description
  type: string
- description: The event type used to train and score.
  name: eventTypeName
  type: string
- description: ''
  name: arn
  type: string
- description: ''
  name: lastUpdatedTime
  type: string
- description: ''
  name: createdTime
  type: string
provider_name: Amazon Fraud Detector
provider_slug: amazon-fraud-detector
schema_file: json-schema/amazon-fraud-detector-model-schema.json
slug: amazon-fraud-detector-model
tags:
- AWS
- Financial Services
- Fraud Detection
- Machine Learning
- Security
title: Model
---
