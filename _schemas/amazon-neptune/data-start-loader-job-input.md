---
description: StartLoaderJobInput schema from Neptune
layout: schema
name: StartLoaderJobInput
properties_list:
- description: Amazon S3 URI identifying files or folders to load (s3://bucket/key).
  name: source
  type: string
- description: The data format of the files to load.
  name: format
  type: string
- description: The ARN of the IAM role with S3 access.
  name: iamRoleArn
  type: string
- description: The AWS Region of the S3 bucket.
  name: region
  type: string
- description: The load mode.
  name: mode
  type: string
- description: Whether to stop the load job on error.
  name: failOnError
  type: string
- description: The degree of parallelism for loading.
  name: parallelism
  type: string
- description: Optional parser configuration settings.
  name: parserConfiguration
  type: object
- description: Whether to update existing single-cardinality properties.
  name: updateSingleCardinalityProperties
  type: string
- description: Whether to queue the request if a load is already running.
  name: queueRequest
  type: string
- description: Load job IDs that must complete before this job runs.
  name: dependencies
  type: array
- description: For openCypher format, whether edge IDs are provided.
  name: userProvidedEdgeIds
  type: string
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/data-start-loader-job-input-schema.json
slug: data-start-loader-job-input
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: StartLoaderJobInput
---
