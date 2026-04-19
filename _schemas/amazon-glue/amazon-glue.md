---
description: Represents an Amazon Glue ETL job with its associated configuration, state, and metadata.
layout: schema
name: Amazon Glue Job
properties_list:
- description: The name of the job
  name: name
  type: string
- description: The IAM role associated with the job
  name: role
  type: string
- description: The job command configuration
  name: command
  type: object
- description: The Glue version to use for the job
  name: glueVersion
  type: string
- description: The type of predefined worker
  name: workerType
  type: string
- description: The number of workers allocated
  name: numberOfWorkers
  type: integer
- description: The maximum number of times to retry a failed job
  name: maxRetries
  type: integer
- description: The job timeout in minutes
  name: timeout
  type: integer
- description: The connections used by the job
  name: connections
  type: object
- description: Default arguments for the job
  name: defaultArguments
  type: object
- description: The time the job was created
  name: createdOn
  type: string
- description: The time the job was last modified
  name: lastModifiedOn
  type: string
provider_name: Amazon Glue
provider_slug: amazon-glue
schema_file: json-schema/amazon-glue-schema.json
slug: amazon-glue
tags:
- Analytics
- AWS
- Data Catalog
- Data Integration
- Data Pipeline
- ETL
- Serverless
title: Amazon Glue Job
---
