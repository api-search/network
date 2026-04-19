---
description: An Amazon Lookout for Equipment ML model for anomaly detection.
layout: schema
name: Model
properties_list:
- description: The name of the model.
  name: ModelName
  type: string
- description: The Amazon Resource Name (ARN) of the model.
  name: ModelArn
  type: string
- description: The name of the dataset used to train the model.
  name: DatasetName
  type: string
- description: The current status of the model.
  name: Status
  type: string
- description: Indicates the time reference in the dataset from which training data begins.
  name: TrainingDataStartTime
  type: string
- description: Indicates the time reference in the dataset from which training data ends.
  name: TrainingDataEndTime
  type: string
- description: The time at which the model was created.
  name: CreatedAt
  type: string
provider_name: Amazon Lookout for Equipment
provider_slug: amazon-lookout-for-equipment
schema_file: json-schema/amazon-lookout-for-equipment-model-schema.json
slug: amazon-lookout-for-equipment-model
tags:
- AWS
- Equipment Monitoring
- Industrial IoT
- Machine Learning
- Predictive Maintenance
title: Model
---
