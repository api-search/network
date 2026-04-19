---
description: An Amazon Forecast output generated from a trained predictor.
layout: schema
name: Forecast
properties_list:
- description: ARN of the forecast.
  name: ForecastArn
  type: string
- description: Name of the forecast.
  name: ForecastName
  type: string
- description: ARN of the predictor used.
  name: PredictorArn
  type: string
- description: Forecast quantiles generated.
  name: ForecastTypes
  type: array
- description: Status of the forecast.
  name: Status
  type: string
- description: ''
  name: CreationTime
  type: string
- description: ''
  name: LastModificationTime
  type: string
provider_name: Amazon Forecast
provider_slug: amazon-forecast
schema_file: json-schema/amazon-forecast-forecast-schema.json
slug: amazon-forecast-forecast
tags:
- AWS
- Forecasting
- Machine Learning
- Predictive Analytics
- Time Series
title: Forecast
---
