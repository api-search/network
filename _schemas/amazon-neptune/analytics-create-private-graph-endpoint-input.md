---
description: CreatePrivateGraphEndpointInput schema from Neptune
layout: schema
name: CreatePrivateGraphEndpointInput
properties_list:
- description: The VPC ID for the private endpoint.
  name: vpcId
  type: string
- description: The subnet IDs for the private endpoint.
  name: subnetIds
  type: array
- description: The security group IDs for the private endpoint.
  name: vpcSecurityGroupIds
  type: array
provider_name: Amazon Neptune
provider_slug: amazon-neptune
schema_file: json-schema/analytics-create-private-graph-endpoint-input-schema.json
slug: analytics-create-private-graph-endpoint-input
tags:
- AWS
- Database
- Graph Database
- Gremlin
- Neptune
- Property Graph
- RDF
- SPARQL
title: CreatePrivateGraphEndpointInput
---
