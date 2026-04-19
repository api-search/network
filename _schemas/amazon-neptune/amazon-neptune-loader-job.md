---
description: Represents a Neptune bulk loader job configuration and its status. The loader ingests data from Amazon S3 into a Neptune DB instance, supporting CSV for property graphs and N-Triples, N-Quads, RDF/XML, and Turtle for RDF data.
layout: schema
name: Amazon Neptune Loader Job
properties_list:
- description: 'Amazon S3 URI identifying the data file(s), folder, or multiple folders to load. Supported URI formats: s3://bucket/key, https://s3.amazonaws.com/bucket/key.'
  name: source
  type: string
- description: The data format of the source files to be loaded.
  name: format
  type: string
- description: The ARN of the IAM role that provides Neptune access to the S3 bucket. Can be a comma-separated list of role ARNs for cross-account access.
  name: iamRoleArn
  type: string
- description: The AWS Region of the S3 bucket containing the data to load.
  name: region
  type: string
- description: The load mode. NEW fails if data was previously loaded. RESUME continues a failed load from where it left off. AUTO resumes if possible, otherwise starts new.
  name: mode
  type: string
- description: Whether to stop the entire load job when an error is encountered.
  name: failOnError
  type: string
- description: The degree of parallelism for loading. LOW uses a single thread, MEDIUM uses num_vCPU/2, HIGH uses num_vCPU, OVERSUBSCRIBE uses all available resources.
  name: parallelism
  type: string
- description: Optional parser configuration settings for RDF data.
  name: parserConfiguration
  type: object
- description: Whether to update existing single-cardinality vertex properties with new values. Not supported for openCypher format.
  name: updateSingleCardinalityProperties
  type: string
- description: Whether to queue the request if a load job is already running. Neptune queues up to 64 jobs in FIFO order.
  name: queueRequest
  type: string
- description: An array of load job IDs that must complete successfully before this job runs.
  name: dependencies
  type: array
- description: For openCypher format only. TRUE means edge files contain an :ID column. FALSE means Neptune auto-generates edge IDs.
  name: userProvidedEdgeIds
  type: string
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/amazon-neptune-loader-job-schema.json
slug: amazon-neptune-loader-job
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: Amazon Neptune Loader Job
---
