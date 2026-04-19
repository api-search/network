---
description: An Amazon Keyspaces table.
layout: schema
name: Table
properties_list:
- description: The name of the keyspace that the table is associated with.
  name: keyspaceName
  type: string
- description: The name of the table.
  name: tableName
  type: string
- description: The Amazon Resource Name (ARN) of the table.
  name: resourceArn
  type: string
- description: The current status of the table.
  name: status
  type: string
- description: The timestamp of when the table was created.
  name: creationTimestamp
  type: string
provider_name: Amazon Keyspaces
provider_slug: amazon-keyspaces
schema_file: json-schema/amazon-keyspaces-table-schema.json
slug: amazon-keyspaces-table
tags:
- AWS
- Cassandra
- Database
- Managed Database
- NoSQL
- Wide Column
title: Table
---
