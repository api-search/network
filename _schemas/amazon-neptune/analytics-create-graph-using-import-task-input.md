---
description: CreateGraphUsingImportTaskInput schema from Neptune
layout: schema
name: CreateGraphUsingImportTaskInput
properties_list:
- description: The name of the graph to create.
  name: graphName
  type: string
- description: S3 URI of the source data to import.
  name: source
  type: string
- description: IAM role ARN with S3 access.
  name: roleArn
  type: string
- description: ''
  name: provisionedMemory
  type: integer
- description: The format of the source data.
  name: format
  type: string
- description: ''
  name: tags
  type: object
- description: ''
  name: deletionProtection
  type: boolean
- description: ''
  name: publicConnectivity
  type: boolean
- description: ''
  name: kmsKeyIdentifier
  type: string
- description: ''
  name: vectorSearchConfiguration
  type: object
- description: ''
  name: replicaCount
  type: integer
- description: Additional import configuration options.
  name: importOptions
  type: object
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/analytics-create-graph-using-import-task-input-schema.json
slug: analytics-create-graph-using-import-task-input
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: CreateGraphUsingImportTaskInput
---
