---
description: ''
layout: schema
name: StatementData
properties_list:
- description: The identifier of the SQL statement
  name: Id
  type: string
- description: The name of the SQL statement
  name: StatementName
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
- description: The SQL statement text
  name: QueryString
  type: string
- description: The query parameters
  name: QueryParameters
  type: array
- description: The name of the database
  name: Database
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
- description: Whether this is a batch statement
  name: IsBatchStatement
  type: boolean
provider_name: Amazon Redshift
provider_slug: amazon-redshift
schema_file: json-schema/amazon-redshift-data-statement-data-schema.json
slug: amazon-redshift-data-statement-data
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
title: StatementData
---
