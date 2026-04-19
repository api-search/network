---
description: TrainingJob schema from Amazon SageMaker API
layout: schema
name: TrainingJob
properties_list:
- description: The name of the training job.
  name: TrainingJobName
  type: string
- description: The Amazon Resource Name (ARN) of the training job.
  name: TrainingJobArn
  type: string
- description: The status of the training job.
  name: TrainingJobStatus
  type: string
- description: Provides detailed information about the state of the training job.
  name: SecondaryStatus
  type: string
- description: ''
  name: AlgorithmSpecification
  type: object
- description: The ARN of the IAM role.
  name: RoleArn
  type: string
- description: ''
  name: InputDataConfig
  type: array
- description: ''
  name: OutputDataConfig
  type: object
- description: ''
  name: ResourceConfig
  type: object
- description: ''
  name: StoppingCondition
  type: object
- description: ''
  name: HyperParameters
  type: object
- description: ''
  name: ModelArtifacts
  type: object
- description: ''
  name: TrainingStartTime
  type: string
- description: ''
  name: TrainingEndTime
  type: string
- description: ''
  name: CreationTime
  type: string
- description: ''
  name: LastModifiedTime
  type: string
- description: ''
  name: BillableTimeInSeconds
  type: integer
- description: ''
  name: FailureReason
  type: string
provider_name: Amazon SageMaker
provider_slug: amazon-sagemaker
schema_file: json-schema/amazon-sagemaker-training-job-schema.json
slug: amazon-sagemaker-training-job
tags:
- AI
- AWS
- Inference
- Machine Learning
- MLOps
- Training
title: TrainingJob
---
