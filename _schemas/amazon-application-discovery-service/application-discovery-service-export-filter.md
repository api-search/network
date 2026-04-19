---
description: ExportFilter schema from Amazon Application Discovery Service API
layout: schema
name: ExportFilter
properties_list:
- description: A single ExportFilter name. Supported filters — agentIds.
  name: name
  type: string
- description: A single agent ID for a Discovery Agent. An agent ID can be found using the DescribeAgents action.
  name: values
  type: array
- description: Supported condition — EQUALS.
  name: condition
  type: string
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-export-filter-schema.json
slug: application-discovery-service-export-filter
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: ExportFilter
---
