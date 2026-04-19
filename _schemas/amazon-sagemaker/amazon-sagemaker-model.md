---
description: Model schema from Amazon SageMaker API
layout: schema
name: Model
properties_list:
- description: The name of the model.
  name: ModelName
  type: string
- description: The Amazon Resource Name (ARN) of the model.
  name: ModelArn
  type: string
- description: ''
  name: PrimaryContainer
  type: object
- description: The ARN of the IAM role.
  name: ExecutionRoleArn
  type: string
- description: A timestamp indicating when the model was created.
  name: CreationTime
  type: string
provider_name: Amazon SageMaker
provider_slug: amazon-sagemaker
schema_file: json-schema/amazon-sagemaker-model-schema.json
slug: amazon-sagemaker-model
tags:
- AI
- AWS
- Inference
- Machine Learning
- MLOps
- Training
title: Model
---
