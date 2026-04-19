---
description: An Amazon Keyspaces keyspace (Cassandra database).
layout: schema
name: Keyspace
properties_list:
- description: The name of the keyspace.
  name: keyspaceName
  type: string
- description: The Amazon Resource Name (ARN) of the keyspace.
  name: resourceArn
  type: string
- description: The replication strategy of the keyspace.
  name: replicationStrategy
  type: string
provider_name: Amazon Keyspaces
provider_slug: amazon-keyspaces
schema_file: json-schema/amazon-keyspaces-keyspace-schema.json
slug: amazon-keyspaces-keyspace
tags:
- AWS
- Cassandra
- Database
- Managed Database
- NoSQL
- Wide Column
title: Keyspace
---
