---
description: CreateDataProcessingJobRequest schema from Neptune
layout: schema
name: CreateDataProcessingJobRequest
properties_list:
- description: Unique identifier for the job (auto-generated UUID if omitted).
  name: id
  type: string
- description: S3 URI for the input data.
  name: inputDataS3Location
  type: string
- description: S3 URI where processed output is written.
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
- description: Disk volume size in GB (default 0 means auto-selected).
  name: processingInstanceVolumeSizeInGB
  type: integer
- description: Timeout in seconds (default 86400, i.e., 1 day).
  name: processingTimeOutInSeconds
  type: integer
- description: The type of model to prepare data for.
  name: modelType
  type: string
- description: The data specification configuration file name.
  name: configFileName
  type: string
- description: VPC subnet IDs for SageMaker processing.
  name: subnets
  type: array
- description: VPC security group IDs.
  name: securityGroupIds
  type: array
- description: KMS key for storage volume encryption.
  name: volumeEncryptionKMSKey
  type: string
- description: KMS key for S3 output encryption.
  name: s3OutputEncryptionKMSKey
  type: string
- description: Whether to enable inter-container traffic encryption.
  name: enableInterContainerTrafficEncryption
  type: boolean
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/ml-create-data-processing-job-request-schema.json
slug: ml-create-data-processing-job-request
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: CreateDataProcessingJobRequest
---
