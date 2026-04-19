---
description: ''
layout: schema
name: DescribeStatementResponse
properties_list:
- description: The identifier of the SQL statement
  name: Id
  type: string
- description: The status of the SQL statement
  name: Status
  type: string
- description: The date and time the statement was created
  name: CreatedAt
  type: string
- description: The date and time the statement was last updated
  name: UpdatedAt
  type: string
- description: The time in nanoseconds the statement ran
  name: Duration
  type: integer
- description: The SQL statement that was executed
  name: QueryString
  type: string
- description: The parameters for the SQL statement
  name: QueryParameters
  type: array
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
- description: The secret ARN
  name: SecretArn
  type: string
- description: The process identifier from the Redshift cluster
  name: RedshiftPid
  type: integer
- description: The Redshift query identifier
  name: RedshiftQueryId
  type: integer
- description: Total number of rows in the result set (FINISHED only)
  name: ResultRows
  type: integer
- description: The size of the result set in bytes
  name: ResultSize
  type: integer
- description: Whether the statement has a result set
  name: HasResultSet
  type: boolean
- description: The error message if the statement failed
  name: Error
  type: string
- description: List of sub-statements for a batch execution. Only present for BatchExecuteStatement calls.
  name: SubStatements
  type: array
provider_name: Amazon Redshift
provider_slug: amazon-redshift
schema_file: json-schema/amazon-redshift-data-describe-statement-response-schema.json
slug: amazon-redshift-data-describe-statement-response
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
title: DescribeStatementResponse
---
