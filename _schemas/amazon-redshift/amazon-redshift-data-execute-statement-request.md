---
description: ''
layout: schema
name: ExecuteStatementRequest
properties_list:
- description: The cluster identifier. Required when connecting to a provisioned cluster. Mutually exclusive with WorkgroupName.
  name: ClusterIdentifier
  type: string
- description: The name of the database to run the SQL statement against
  name: Database
  type: string
- description: The database user name. Required when authenticating with temporary credentials from GetClusterCredentials.
  name: DbUser
  type: string
- description: The ARN of the secret stored in AWS Secrets Manager that contains the database credentials. Mutually exclusive with DbUser and temporary credentials.
  name: SecretArn
  type: string
- description: The SQL statement to run. Maximum length is 100,000 characters.
  name: Sql
  type: string
- description: A name for the SQL statement. This name can be used to identify the query in the ListStatements output.
  name: StatementName
  type: string
- description: Whether to send an event to Amazon EventBridge when the SQL statement completes. Default is false.
  name: WithEvent
  type: boolean
- description: The serverless workgroup name. Required when connecting to Redshift Serverless. Mutually exclusive with ClusterIdentifier.
  name: WorkgroupName
  type: string
- description: Named parameters for the SQL statement. Use :name syntax in the SQL string to reference parameters.
  name: Parameters
  type: array
- description: A unique, case-sensitive identifier to ensure idempotency of the request.
  name: ClientToken
  type: string
provider_name: Amazon Redshift
provider_slug: amazon-redshift
schema_file: json-schema/amazon-redshift-data-execute-statement-request-schema.json
slug: amazon-redshift-data-execute-statement-request
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
title: ExecuteStatementRequest
---
