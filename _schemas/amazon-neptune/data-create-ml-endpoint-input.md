---
description: CreateMLEndpointInput schema from Neptune
layout: schema
name: CreateMLEndpointInput
properties_list:
- description: Unique identifier for the endpoint.
  name: id
  type: string
- description: Job ID from a completed training job.
  name: mlModelTrainingJobId
  type: string
- description: Job ID from a completed transform job.
  name: mlModelTransformJobId
  type: string
- description: Whether this is an update request.
  name: update
  type: boolean
- description: ''
  name: neptuneIamRoleArn
  type: string
- description: ''
  name: modelName
  type: string
- description: ''
  name: instanceType
  type: string
- description: ''
  name: instanceCount
  type: integer
- description: ''
  name: volumeEncryptionKMSKey
  type: string
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/data-create-ml-endpoint-input-schema.json
slug: data-create-ml-endpoint-input
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: CreateMLEndpointInput
---
