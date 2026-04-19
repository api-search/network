---
description: StartMLModelTransformJobInput schema from Neptune
layout: schema
name: StartMLModelTransformJobInput
properties_list:
- description: ''
  name: id
  type: string
- description: ''
  name: dataProcessingJobId
  type: string
- description: ''
  name: mlModelTrainingJobId
  type: string
- description: ''
  name: trainingJobName
  type: string
- description: S3 location for transform output.
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
schema_file: json-schema/data-start-ml-model-transform-job-input-schema.json
slug: data-start-ml-model-transform-job-input
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: StartMLModelTransformJobInput
---
