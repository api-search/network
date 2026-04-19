---
description: CreateModelTrainingJobRequest schema from Neptune
layout: schema
name: CreateModelTrainingJobRequest
properties_list:
- description: Unique identifier for the job.
  name: id
  type: string
- description: Job ID of the completed data processing job.
  name: dataProcessingJobId
  type: string
- description: S3 location for model artifacts output.
  name: trainModelS3Location
  type: string
- description: Job ID of a previous training job for incremental training.
  name: previousModelTrainingJobId
  type: string
- description: ''
  name: sagemakerIamRoleArn
  type: string
- description: ''
  name: neptuneIamRoleArn
  type: string
- description: 'The model type to train: rgcn (relational graph convolutional network), transe, distmult, rotate, or custom.'
  name: modelName
  type: string
- description: ML instance type for data preparation step.
  name: baseProcessingInstanceType
  type: string
- description: ML instance type for the training step.
  name: trainingInstanceType
  type: string
- description: Disk volume size for training instance in GB.
  name: trainingInstanceVolumeSizeInGB
  type: integer
- description: Training job timeout in seconds.
  name: trainingTimeOutInSeconds
  type: integer
- description: Maximum total training jobs for hyperparameter tuning. Minimum 10 recommended for meaningful results.
  name: maxHPONumberOfTrainingJobs
  type: integer
- description: Maximum parallel training jobs.
  name: maxHPOParallelTrainingJobs
  type: integer
- description: ''
  name: subnets
  type: array
- description: ''
  name: securityGroupIds
  type: array
- description: ''
  name: volumeEncryptionKMSKey
  type: string
- description: ''
  name: s3OutputEncryptionKMSKey
  type: string
- description: ''
  name: enableInterContainerTrafficEncryption
  type: boolean
- description: Whether to use EC2 spot instances for training.
  name: enableManagedSpotTraining
  type: boolean
- description: Custom model training configuration.
  name: customModelTrainingParameters
  type: object
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/ml-create-model-training-job-request-schema.json
slug: ml-create-model-training-job-request
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: CreateModelTrainingJobRequest
---
