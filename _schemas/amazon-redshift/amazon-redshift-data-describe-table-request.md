---
description: ''
layout: schema
name: DescribeTableRequest
properties_list:
- description: The cluster identifier
  name: ClusterIdentifier
  type: string
- description: The name of the database
  name: Database
  type: string
- description: The database user for temporary credentials
  name: DbUser
  type: string
- description: ARN of the secret in Secrets Manager
  name: SecretArn
  type: string
- description: The serverless workgroup name
  name: WorkgroupName
  type: string
- description: The table name. Can be qualified with schema name as schema_name.table_name.
  name: Table
  type: string
- description: The schema that contains the table. Default is public.
  name: Schema
  type: string
- description: Maximum number of columns to return
  name: MaxResults
  type: integer
- description: Pagination token for the next page
  name: NextToken
  type: string
provider_name: Amazon Redshift
provider_slug: amazon-redshift
schema_file: json-schema/amazon-redshift-data-describe-table-request-schema.json
slug: amazon-redshift-data-describe-table-request
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
title: DescribeTableRequest
---
