---
description: CreateModelTransformJobRequest schema from Neptune
layout: schema
name: CreateModelTransformJobRequest
properties_list:
- description: ''
  name: id
  type: string
- description: Job ID of the completed data processing job.
  name: dataProcessingJobId
  type: string
- description: Job ID of the completed model training job.
  name: mlModelTrainingJobId
  type: string
- description: Name of a completed SageMaker training job.
  name: trainingJobName
  type: string
- description: S3 location for transform output artifacts.
  name: modelTransformOutputS3Location
  type: string
- description: ''
  name: sagemakerIamRoleArn
  type: string
- description: ''
  name: neptuneIamRoleArn
  type: string
- description: ''
  name: baseProcessingInstanceType
  type: string
- description: ''
  name: baseProcessingInstanceVolumeSizeInGB
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
  name: customModelTransformParameters
  type: object
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/ml-create-model-transform-job-request-schema.json
slug: ml-create-model-transform-job-request
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: CreateModelTransformJobRequest
---
