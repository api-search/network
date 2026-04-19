---
class_count: 5
classes:
- Dataset
- Predictor
- Forecast
- DatasetGroup
- Tag
context_file: json-ld/amazon-forecast-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-forecast/refs/heads/main/json-ld/amazon-forecast-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Forecast from Amazon Forecast.
layout: jsonld
name: Amazon Forecast Context
namespaces:
- prefix: forecast
  uri: https://aws.amazon.com/forecast/vocabulary/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: DatasetArn
  type: string
- container: ''
  name: DatasetName
  type: string
- container: ''
  name: Domain
  type: string
- container: ''
  name: DatasetType
  type: string
- container: ''
  name: DataFrequency
  type: string
- container: ''
  name: PredictorArn
  type: string
- container: ''
  name: PredictorName
  type: string
- container: ''
  name: ForecastHorizon
  type: integer
- container: ''
  name: ForecastArn
  type: string
- container: ''
  name: ForecastName
  type: string
- container: ''
  name: Status
  type: string
- container: ''
  name: CreationTime
  type: dateTime
- container: ''
  name: LastModificationTime
  type: dateTime
- container: ''
  name: Key
  type: string
- container: ''
  name: Value
  type: string
property_count: 15
provider_name: Amazon Forecast
provider_slug: amazon-forecast
slug: amazon-forecast-context
tags:
- AWS
- Forecasting
- Machine Learning
- Predictive Analytics
- Time Series
- JSON-LD
- Linked Data
- Semantic Web
---
