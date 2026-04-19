---
description: A member instance of a Neptune DB cluster.
layout: schema
name: DBClusterMember
properties_list:
- description: The instance identifier.
  name: DBInstanceIdentifier
  type: string
- description: Whether the instance is the primary (writer) instance.
  name: IsClusterWriter
  type: boolean
- description: The status of the parameter group for this member.
  name: DBClusterParameterGroupStatus
  type: string
- description: Failover priority for the instance.
  name: PromotionTier
  type: integer
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/management-db-cluster-member-schema.json
slug: management-db-cluster-member
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: DBClusterMember
---
