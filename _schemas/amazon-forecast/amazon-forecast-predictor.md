---
description: An Amazon Forecast ML predictor trained on a dataset group.
layout: schema
name: Predictor
properties_list:
- description: ARN of the predictor.
  name: PredictorArn
  type: string
- description: Name of the predictor.
  name: PredictorName
  type: string
- description: ARN of the algorithm used.
  name: AlgorithmArn
  type: string
- description: Number of time steps for the forecast.
  name: ForecastHorizon
  type: integer
- description: Quantiles to forecast (e.g., p10, p50, p90).
  name: ForecastTypes
  type: array
- description: Whether to auto-select the best algorithm.
  name: PerformAutoML
  type: boolean
- description: Whether to perform hyperparameter optimization.
  name: PerformHPO
  type: boolean
- description: Status of the predictor.
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
schema_file: json-schema/amazon-forecast-predictor-schema.json
slug: amazon-forecast-predictor
tags:
- AWS
- Forecasting
- Machine Learning
- Predictive Analytics
- Time Series
title: Predictor
---
