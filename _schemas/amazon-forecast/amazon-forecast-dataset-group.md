---
description: A logical grouping of Amazon Forecast datasets for training a predictor.
layout: schema
name: DatasetGroup
properties_list:
- description: ARN of the dataset group.
  name: DatasetGroupArn
  type: string
- description: Name of the dataset group.
  name: DatasetGroupName
  type: string
- description: Domain of the dataset group.
  name: Domain
  type: string
- description: ARNs of datasets in this group.
  name: DatasetArns
  type: array
- description: ''
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
schema_file: json-schema/amazon-forecast-dataset-group-schema.json
slug: amazon-forecast-dataset-group
tags:
- AWS
- Forecasting
- Machine Learning
- Predictive Analytics
- Time Series
title: DatasetGroup
---
