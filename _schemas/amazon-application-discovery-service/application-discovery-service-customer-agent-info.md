---
description: CustomerAgentInfo schema from Amazon Application Discovery Service API
layout: schema
name: CustomerAgentInfo
properties_list:
- description: Number of active discovery agents.
  name: activeAgents
  type: integer
- description: Number of healthy discovery agents.
  name: healthyAgents
  type: integer
- description: Number of blacklisted discovery agents.
  name: blackListedAgents
  type: integer
- description: Number of discovery agents with status SHUTDOWN.
  name: shutdownAgents
  type: integer
- description: Number of unhealthy discovery agents.
  name: unhealthyAgents
  type: integer
- description: Total number of discovery agents.
  name: totalAgents
  type: integer
- description: Number of unknown discovery agents.
  name: unknownAgents
  type: integer
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-customer-agent-info-schema.json
slug: application-discovery-service-customer-agent-info
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: CustomerAgentInfo
---
