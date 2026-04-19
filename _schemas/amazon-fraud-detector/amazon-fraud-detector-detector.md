---
description: An Amazon Fraud Detector that orchestrates ML models and business rules for real-time fraud decisions.
layout: schema
name: Detector
properties_list:
- description: Unique identifier for the detector.
  name: detectorId
  type: string
- description: Optional description of the detector.
  name: description
  type: string
- description: The name of the event type associated with the detector.
  name: eventTypeName
  type: string
- description: ''
  name: lastUpdatedTime
  type: string
- description: ''
  name: createdTime
  type: string
- description: ARN of the detector.
  name: arn
  type: string
provider_name: Amazon Fraud Detector
provider_slug: amazon-fraud-detector
schema_file: json-schema/amazon-fraud-detector-detector-schema.json
slug: amazon-fraud-detector-detector
tags:
- AWS
- Financial Services
- Fraud Detection
- Machine Learning
- Security
title: Detector
---
