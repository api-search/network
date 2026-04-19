---
description: ListServerNeighborsResponse schema from Amazon Application Discovery Service API
layout: schema
name: ListServerNeighborsResponse
properties_list:
- description: List of distinct servers that are one hop away from the given server.
  name: neighbors
  type: array
- description: Token to retrieve the next set of results.
  name: nextToken
  type: string
- description: Count of distinct servers that are one hop away from the given server.
  name: knownDependencyCount
  type: integer
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-list-server-neighbors-response-schema.json
slug: application-discovery-service-list-server-neighbors-response
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: ListServerNeighborsResponse
---
