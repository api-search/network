---
description: ListServerNeighborsRequest schema from Amazon Application Discovery Service API
layout: schema
name: ListServerNeighborsRequest
properties_list:
- description: Configuration ID of the server for which neighbors are being listed.
  name: configurationId
  type: string
- description: Flag to indicate if port and protocol information is needed as part of the response.
  name: portInformationNeeded
  type: boolean
- description: List of configuration IDs to test for one-hop-away. Mandatory parameter when PortInformationNeeded is true.
  name: neighborConfigurationIds
  type: array
- description: Maximum number of results to return in a single page of output.
  name: maxResults
  type: integer
- description: Token to retrieve the next set of results.
  name: nextToken
  type: string
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-list-server-neighbors-request-schema.json
slug: application-discovery-service-list-server-neighbors-request
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: ListServerNeighborsRequest
---
