---
description: CreateInferenceEndpointRequest schema from Neptune
layout: schema
name: CreateInferenceEndpointRequest
properties_list:
- description: Unique identifier for the endpoint (auto-generated timestamped name if omitted).
  name: id
  type: string
- description: Job ID from a completed training job.
  name: mlModelTrainingJobId
  type: string
- description: Job ID from a completed transform job.
  name: mlModelTransformJobId
  type: string
- description: Whether this is an update to an existing endpoint.
  name: update
  type: boolean
- description: ''
  name: neptuneIamRoleArn
  type: string
- description: The model type.
  name: modelName
  type: string
- description: ML instance type for the inference endpoint.
  name: instanceType
  type: string
- description: Minimum number of EC2 instances to deploy.
  name: instanceCount
  type: integer
- description: ''
  name: volumeEncryptionKMSKey
  type: string
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/ml-create-inference-endpoint-request-schema.json
slug: ml-create-inference-endpoint-request
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: CreateInferenceEndpointRequest
---
