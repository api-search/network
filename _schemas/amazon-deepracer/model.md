---
description: A reinforcement learning model trained for DeepRacer autonomous racing.
layout: schema
name: Model
properties_list:
- description: The ARN uniquely identifying the reinforcement learning model.
  name: modelArn
  type: string
- description: The display name of the model.
  name: modelName
  type: string
- description: Timestamp when the model was created.
  name: creationTime
  type: string
- description: Timestamp when the model was last updated.
  name: lastModifiedTime
  type: string
- description: Current status of the model.
  name: modelStatus
  type: string
- description: ARN of the SageMaker training job that produced this model.
  name: trainingJobArn
  type: string
- description: Python reward function code used during training.
  name: rewardFunction
  type: string
provider_name: Amazon DeepRacer
provider_slug: amazon-deepracer
schema_file: json-schema/model-schema.json
slug: model
tags:
- Autonomous Vehicles
- AWS
- Machine Learning
- Reinforcement Learning
- Robotics
title: Model
---
