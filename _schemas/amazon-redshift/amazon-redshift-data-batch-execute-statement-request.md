---
description: ''
layout: schema
name: BatchExecuteStatementRequest
properties_list:
- description: The cluster identifier for a provisioned cluster
  name: ClusterIdentifier
  type: string
- description: The name of the database
  name: Database
  type: string
- description: The database user name for temporary credentials
  name: DbUser
  type: string
- description: ARN of the secret in AWS Secrets Manager
  name: SecretArn
  type: string
- description: One or more SQL statements to run. The statements run serially as a single transaction. Maximum 40 statements.
  name: Sqls
  type: array
- description: A name for the batch SQL statement
  name: StatementName
  type: string
- description: Whether to send an event to EventBridge on completion
  name: WithEvent
  type: boolean
- description: The serverless workgroup name
  name: WorkgroupName
  type: string
- description: Idempotency token
  name: ClientToken
  type: string
provider_name: Amazon Redshift
provider_slug: amazon-redshift
schema_file: json-schema/amazon-redshift-data-batch-execute-statement-request-schema.json
slug: amazon-redshift-data-batch-execute-statement-request
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
title: BatchExecuteStatementRequest
---
