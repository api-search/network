---
description: DescribeAgentsRequest schema from Amazon Application Discovery Service API
layout: schema
name: DescribeAgentsRequest
properties_list:
- description: The agent or the collector IDs for which you want information. If you specify no IDs, the system returns information about all agents/collectors associated with your AWS user account.
  name: agentIds
  type: array
- description: You can filter the request using various logical operators and a key-value format.
  name: filters
  type: array
- description: The total number of agents/collectors to return in a single page of output.
  name: maxResults
  type: integer
- description: Token to retrieve the next set of results.
  name: nextToken
  type: string
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-describe-agents-request-schema.json
slug: application-discovery-service-describe-agents-request
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: DescribeAgentsRequest
---
