---
description: Schema defining the structure of an AWS Batch job definition resource, including container properties, retry strategy, timeout, scheduling, and resource requirements.
layout: schema
name: AWS Batch Job Definition
properties_list:
- description: The name of the job definition.
  name: jobDefinitionName
  type: string
- description: The Amazon Resource Name (ARN) for the job definition.
  name: jobDefinitionArn
  type: string
- description: The revision of the job definition.
  name: revision
  type: integer
- description: The status of the job definition.
  name: status
  type: string
- description: The type of job definition.
  name: type
  type: string
- description: The scheduling priority of the job definition.
  name: schedulingPriority
  type: integer
- description: Default parameters or parameter substitution placeholders in the job definition.
  name: parameters
  type: object
- description: ''
  name: retryStrategy
  type: object
- description: ''
  name: containerProperties
  type: object
- description: ''
  name: nodeProperties
  type: object
- description: ''
  name: timeout
  type: object
- description: The tags that are applied to the job definition.
  name: tags
  type: object
- description: The platform capabilities required by the job definition.
  name: platformCapabilities
  type: array
- description: Whether to propagate tags from the job definition to the job.
  name: propagateTags
  type: boolean
provider_name: Amazon Batch
provider_slug: amazon-batch
schema_file: json-schema/amazon-batch-schema.json
slug: amazon-batch
tags:
- AWS
- Batch Computing
- Compute
- Containers
- HPC
- Job Scheduling
- Serverless
- Fargate
- EKS
- Spot Instances
title: AWS Batch Job Definition
---
