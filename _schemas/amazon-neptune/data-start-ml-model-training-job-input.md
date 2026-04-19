---
description: StartMLModelTrainingJobInput schema from Neptune
layout: schema
name: StartMLModelTrainingJobInput
properties_list:
- description: ''
  name: id
  type: string
- description: Job ID of the completed data processing job.
  name: dataProcessingJobId
  type: string
- description: S3 location for model artifacts.
  name: trainModelS3Location
  type: string
- description: ''
  name: previousModelTrainingJobId
  type: string
- description: ''
  name: sagemakerIamRoleArn
  type: string
- description: ''
  name: neptuneIamRoleArn
  type: string
- description: The model type to use.
  name: modelName
  type: string
- description: ''
  name: baseProcessingInstanceType
  type: string
- description: ''
  name: trainingInstanceType
  type: string
- description: ''
  name: trainingInstanceVolumeSizeInGB
  type: integer
- description: ''
  name: trainingTimeOutInSeconds
  type: integer
- description: ''
  name: maxHPONumberOfTrainingJobs
  type: integer
- description: ''
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
- description: ''
  name: enableManagedSpotTraining
  type: boolean
- description: ''
  name: customModelTrainingParameters
  type: object
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/data-start-ml-model-training-job-input-schema.json
slug: data-start-ml-model-training-job-input
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: StartMLModelTrainingJobInput
---
