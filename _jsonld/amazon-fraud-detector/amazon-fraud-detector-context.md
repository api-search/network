---
class_count: 5
classes:
- Detector
- Model
- Rule
- EventType
- Tag
context_file: json-ld/amazon-fraud-detector-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-fraud-detector/refs/heads/main/json-ld/amazon-fraud-detector-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Fraud Detector from Amazon Fraud Detector.
layout: jsonld
name: Amazon Fraud Detector Context
namespaces:
- prefix: fd
  uri: https://aws.amazon.com/fraud-detector/vocabulary/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: detectorId
  type: string
- container: ''
  name: modelId
  type: string
- container: ''
  name: modelType
  type: string
- container: ''
  name: ruleId
  type: string
- container: ''
  name: expression
  type: string
- container: ''
  name: outcomes
  type: ''
- container: ''
  name: eventTypeName
  type: string
- container: ''
  name: eventVariables
  type: ''
- container: ''
  name: labels
  type: ''
- container: ''
  name: arn
  type: string
- container: ''
  name: createdTime
  type: dateTime
- container: ''
  name: lastUpdatedTime
  type: dateTime
property_count: 12
provider_name: Amazon Fraud Detector
provider_slug: amazon-fraud-detector
slug: amazon-fraud-detector-context
tags:
- AWS
- Financial Services
- Fraud Detection
- Machine Learning
- Security
- JSON-LD
- Linked Data
- Semantic Web
---
