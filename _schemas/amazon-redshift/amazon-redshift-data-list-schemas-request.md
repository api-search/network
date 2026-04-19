---
description: ''
layout: schema
name: ListSchemasRequest
properties_list:
- description: The cluster identifier
  name: ClusterIdentifier
  type: string
- description: The name of the database containing the schemas
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
- description: A pattern to filter schemas. Uses SQL LIKE syntax where underscore matches one character and percent matches zero or more characters.
  name: SchemaPattern
  type: string
- description: Maximum number of schemas to return
  name: MaxResults
  type: integer
- description: Pagination token for the next page
  name: NextToken
  type: string
provider_name: Amazon Redshift
provider_slug: amazon-redshift
schema_file: json-schema/amazon-redshift-data-list-schemas-request-schema.json
slug: amazon-redshift-data-list-schemas-request
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
title: ListSchemasRequest
---
