---
description: ''
layout: schema
name: ListStatementsRequest
properties_list:
- description: The maximum number of SQL statements to return in the response. Valid range is 0 to 100. Default is 100.
  name: MaxResults
  type: integer
- description: A value that indicates the starting point for the next set of response records in a subsequent request.
  name: NextToken
  type: string
- description: When true, returns statements submitted by all IAM users in the account. Default is false, which returns only statements from the calling user.
  name: RoleLevel
  type: boolean
- description: Filter results by a specific statement name
  name: StatementName
  type: string
- description: Filter results by statement status
  name: Status
  type: string
provider_name: Amazon Redshift
provider_slug: amazon-redshift
schema_file: json-schema/amazon-redshift-data-list-statements-request-schema.json
slug: amazon-redshift-data-list-statements-request
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
title: ListStatementsRequest
---
