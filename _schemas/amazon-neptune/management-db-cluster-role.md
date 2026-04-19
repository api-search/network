---
description: An IAM role associated with a Neptune DB cluster.
layout: schema
name: DBClusterRole
properties_list:
- description: The ARN of the IAM role.
  name: RoleArn
  type: string
- description: The status of the association (active, pending, error).
  name: Status
  type: string
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/management-db-cluster-role-schema.json
slug: management-db-cluster-role
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: DBClusterRole
---
