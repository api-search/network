---
class_count: 10
classes:
- CreateDataProcessingJobRequest
- CreateInferenceEndpointRequest
- CreateModelTrainingJobRequest
- CreateModelTransformJobRequest
- EndpointCreatedResponse
- EndpointListResponse
- EndpointStatusResponse
- JobCreatedResponse
- JobListResponse
- JobStatusResponse
context_file: json-ld/amazon-neptune-ml-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-neptune/refs/heads/main/json-ld/amazon-neptune-ml-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Neptune Ml from Amazon Neptune.
layout: jsonld
name: Amazon Neptune Ml Context
namespaces:
- prefix: neptune
  uri: https://neptune.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: arn
  type: string
- container: ''
  name: baseProcessingInstanceType
  type: string
- container: ''
  name: baseProcessingInstanceVolumeSizeInGB
  type: integer
- container: ''
  name: cloudwatchLogUrl
  type: string
- container: ''
  name: configFileName
  type: string
- container: ''
  name: customModelTrainingParameters
  type: reference
- container: ''
  name: customModelTransformParameters
  type: reference
- container: ''
  name: dataProcessingJobId
  type: string
- container: ''
  name: enableInterContainerTrafficEncryption
  type: boolean
- container: ''
  name: enableManagedSpotTraining
  type: boolean
- container: ''
  name: endpoint
  type: reference
- container: ''
  name: endpointConfig
  type: reference
- container: ''
  name: failureReason
  type: string
- container: ''
  name: id
  type: string
- container: set
  name: ids
  type: string
- container: ''
  name: inputDataS3Location
  type: string
- container: ''
  name: instanceCount
  type: integer
- container: ''
  name: instanceType
  type: string
- container: ''
  name: maxHPONumberOfTrainingJobs
  type: integer
- container: ''
  name: maxHPOParallelTrainingJobs
  type: integer
- container: ''
  name: mlModelTrainingJobId
  type: string
- container: ''
  name: mlModelTransformJobId
  type: string
- container: ''
  name: modelName
  type: string
- container: ''
  name: modelTransformOutputS3Location
  type: string
- container: ''
  name: modelType
  type: string
- container: ''
  name: name
  type: ''
- container: ''
  name: neptuneIamRoleArn
  type: string
- container: ''
  name: outputLocation
  type: string
- container: ''
  name: previousDataProcessingJobId
  type: string
- container: ''
  name: previousModelTrainingJobId
  type: string
- container: ''
  name: processedDataS3Location
  type: string
- container: ''
  name: processingInstanceType
  type: string
- container: ''
  name: processingInstanceVolumeSizeInGB
  type: integer
- container: ''
  name: processingJob
  type: reference
- container: ''
  name: processingTimeOutInSeconds
  type: integer
- container: ''
  name: s3OutputEncryptionKMSKey
  type: string
- container: ''
  name: sagemakerIamRoleArn
  type: string
- container: set
  name: securityGroupIds
  type: string
- container: ''
  name: sourceS3DirectoryPath
  type: string
- container: ''
  name: status
  type: string
- container: set
  name: subnets
  type: string
- container: ''
  name: trainModelS3Location
  type: string
- container: ''
  name: trainingEntryPointScript
  type: string
- container: ''
  name: trainingInstanceType
  type: string
- container: ''
  name: trainingInstanceVolumeSizeInGB
  type: integer
- container: ''
  name: trainingJobName
  type: string
- container: ''
  name: trainingTimeOutInSeconds
  type: integer
- container: ''
  name: transformEntryPointScript
  type: string
- container: ''
  name: update
  type: boolean
- container: ''
  name: volumeEncryptionKMSKey
  type: string
property_count: 50
provider_name: Amazon Neptune
provider_slug: amazon-neptune
slug: amazon-neptune-ml-context
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
- JSON-LD
- Linked Data
- Semantic Web
---
