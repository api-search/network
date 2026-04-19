---
description: StartMLDataProcessingJobInput schema from Neptune
layout: schema
name: StartMLDataProcessingJobInput
properties_list:
- description: Unique identifier for the job (auto-generated if omitted).
  name: id
  type: string
- description: S3 URI for input data.
  name: inputDataS3Location
  type: string
- description: S3 URI for output results.
  name: processedDataS3Location
  type: string
- description: Job ID of a previous job for incremental processing.
  name: previousDataProcessingJobId
  type: string
- description: IAM role ARN for SageMaker execution.
  name: sagemakerIamRoleArn
  type: string
- description: IAM role ARN for Neptune access.
  name: neptuneIamRoleArn
  type: string
- description: ML instance type (default auto-selected ml.r5 type).
  name: processingInstanceType
  type: string
- description: Disk volume size in GB (default 0 = auto-selected).
  name: processingInstanceVolumeSizeInGB
  type: integer
- description: Timeout in seconds (default 86400).
  name: processingTimeOutInSeconds
  type: integer
- description: Model type selection.
  name: modelType
  type: string
- description: Data specification file name.
  name: configFileName
  type: string
- description: Subnet IDs in Neptune VPC.
  name: subnets
  type: array
- description: VPC security group IDs.
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
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/data-start-ml-data-processing-job-input-schema.json
slug: data-start-ml-data-processing-job-input
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: StartMLDataProcessingJobInput
---
