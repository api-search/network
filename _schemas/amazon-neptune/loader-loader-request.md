---
description: LoaderRequest schema from Neptune
layout: schema
name: LoaderRequest
properties_list:
- description: 'Amazon S3 URI identifying the data file(s), folder, or multiple folders to load. Supported URI formats: s3://bucket_name/key, https://s3.amazonaws.com/bucket_name/key, https://s3.region.amazonaws.com/'
  name: source
  type: string
- description: The data format of the source files.
  name: format
  type: string
- description: The ARN of the IAM role that provides Neptune access to the S3 bucket. Can be a comma-separated list for cross-account access.
  name: iamRoleArn
  type: string
- description: The AWS Region of the S3 bucket. Must match the Neptune cluster region or be accessible cross-region.
  name: region
  type: string
- description: The load mode. NEW fails if data was previously loaded. RESUME continues a failed load. AUTO resumes or starts new as needed.
  name: mode
  type: string
- description: Whether to stop the entire load job on error.
  name: failOnError
  type: string
- description: The degree of parallelism for loading. LOW uses a single thread, MEDIUM uses num_vCPU/2, HIGH uses num_vCPU, OVERSUBSCRIBE uses all available resources.
  name: parallelism
  type: string
- description: Optional parser configuration settings for RDF data.
  name: parserConfiguration
  type: object
- description: Whether to update existing single-cardinality vertex properties. Not supported for openCypher format.
  name: updateSingleCardinalityProperties
  type: string
- description: Whether to queue the request if a load is already running. Neptune queues up to 64 jobs in FIFO order.
  name: queueRequest
  type: string
- description: Array of load job IDs that must complete successfully before this job runs.
  name: dependencies
  type: array
- description: For openCypher format only. TRUE requires an :ID column in edge files. FALSE auto-generates edge IDs.
  name: userProvidedEdgeIds
  type: string
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/loader-loader-request-schema.json
slug: loader-loader-request
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: LoaderRequest
---
