---
description: ''
layout: schema
name: BatchExecuteStatementResponse
properties_list:
- description: The identifier of the batch SQL statement
  name: Id
  type: string
- description: The date and time the batch statement was created
  name: CreatedAt
  type: string
- description: The name of the database
  name: Database
  type: string
- description: The database user
  name: DbUser
  type: string
- description: The cluster identifier
  name: ClusterIdentifier
  type: string
- description: The serverless workgroup name
  name: WorkgroupName
  type: string
- description: The secret ARN used for authentication
  name: SecretArn
  type: string
provider_name: Amazon Redshift
provider_slug: amazon-redshift
schema_file: json-schema/amazon-redshift-data-batch-execute-statement-response-schema.json
slug: amazon-redshift-data-batch-execute-statement-response
tags:
- Analytics
- Big Data
- Cloud
- Data Lake
- Data Warehouse
- ETL
- Machine Learning
- Serverless
- SQL
title: BatchExecuteStatementResponse
---
