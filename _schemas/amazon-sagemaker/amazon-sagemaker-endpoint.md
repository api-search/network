---
description: Endpoint schema from Amazon SageMaker API
layout: schema
name: Endpoint
properties_list:
- description: The name of the endpoint.
  name: EndpointName
  type: string
- description: The Amazon Resource Name (ARN) of the endpoint.
  name: EndpointArn
  type: string
- description: The name of the endpoint configuration.
  name: EndpointConfigName
  type: string
- description: The status of the endpoint.
  name: EndpointStatus
  type: string
- description: An array of production variants.
  name: ProductionVariants
  type: array
- description: A timestamp indicating when the endpoint was created.
  name: CreationTime
  type: string
- description: A timestamp indicating when the endpoint was last modified.
  name: LastModifiedTime
  type: string
- description: If the status is Failed, the reason it failed.
  name: FailureReason
  type: string
provider_name: Amazon SageMaker
provider_slug: amazon-sagemaker
schema_file: json-schema/amazon-sagemaker-endpoint-schema.json
slug: amazon-sagemaker-endpoint
tags:
- AI
- AWS
- Inference
- Machine Learning
- MLOps
- Training
title: Endpoint
---
