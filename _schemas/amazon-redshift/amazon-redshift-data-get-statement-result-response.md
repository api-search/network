---
description: ''
layout: schema
name: GetStatementResultResponse
properties_list:
- description: The results of the SQL statement as an array of rows
  name: Records
  type: array
- description: Metadata about the columns in the result set
  name: ColumnMetadata
  type: array
- description: Total number of rows in the result set
  name: TotalNumRows
  type: integer
- description: Pagination token for the next page of results
  name: NextToken
  type: string
provider_name: Amazon Redshift
provider_slug: amazon-redshift
schema_file: json-schema/amazon-redshift-data-get-statement-result-response-schema.json
slug: amazon-redshift-data-get-statement-result-response
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
title: GetStatementResultResponse
---
