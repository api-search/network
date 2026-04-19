---
description: GetDiscoverySummaryResponse schema from Amazon Application Discovery Service API
layout: schema
name: GetDiscoverySummaryResponse
properties_list:
- description: The number of servers discovered.
  name: servers
  type: integer
- description: The number of applications discovered.
  name: applications
  type: integer
- description: The number of servers mapped to applications.
  name: serversMappedToApplications
  type: integer
- description: The number of servers mapped to tags.
  name: serversMappedtoTags
  type: integer
- description: The number of servers mapped to applications or tags.
  name: mappedServerCount
  type: integer
- description: The number of servers not mapped to any application.
  name: unmappedServerCount
  type: integer
- description: ''
  name: agentSummary
  type: object
- description: ''
  name: connectorSummary
  type: object
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-get-discovery-summary-response-schema.json
slug: application-discovery-service-get-discovery-summary-response
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: GetDiscoverySummaryResponse
---
