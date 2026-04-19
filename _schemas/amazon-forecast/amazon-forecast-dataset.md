---
description: An Amazon Forecast dataset containing time-series training data.
layout: schema
name: Dataset
properties_list:
- description: ARN of the dataset.
  name: DatasetArn
  type: string
- description: Name of the dataset.
  name: DatasetName
  type: string
- description: Domain for the dataset.
  name: Domain
  type: string
- description: Type of the dataset.
  name: DatasetType
  type: string
- description: Frequency of data points (e.g., D for daily, H for hourly).
  name: DataFrequency
  type: string
- description: Status of the dataset.
  name: Status
  type: string
- description: Time the dataset was created.
  name: CreationTime
  type: string
- description: Time the dataset was last modified.
  name: LastModificationTime
  type: string
provider_name: Amazon Forecast
provider_slug: amazon-forecast
schema_file: json-schema/amazon-forecast-dataset-schema.json
slug: amazon-forecast-dataset
tags:
- AWS
- Forecasting
- Machine Learning
- Predictive Analytics
- Time Series
title: Dataset
---
