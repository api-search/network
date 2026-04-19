---
description: ModifyDBInstanceRequest schema from Neptune
layout: schema
name: ModifyDBInstanceRequest
properties_list:
- description: The DB instance identifier.
  name: DBInstanceIdentifier
  type: string
- description: The new compute and memory capacity.
  name: DBInstanceClass
  type: string
- description: ''
  name: PreferredMaintenanceWindow
  type: string
- description: ''
  name: AutoMinorVersionUpgrade
  type: boolean
- description: ''
  name: NewDBInstanceIdentifier
  type: string
- description: ''
  name: PromotionTier
  type: integer
- description: ''
  name: ApplyImmediately
  type: boolean
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/management-modify-db-instance-request-schema.json
slug: management-modify-db-instance-request
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: ModifyDBInstanceRequest
---
