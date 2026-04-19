---
description: AgentConfigurationStatus schema from Amazon Application Discovery Service API
layout: schema
name: AgentConfigurationStatus
properties_list:
- description: The agent ID.
  name: agentId
  type: string
- description: Information about the status of the StartDataCollection and StopDataCollection operations.
  name: operationSucceeded
  type: boolean
- description: A description of the operation performed.
  name: description
  type: string
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-agent-configuration-status-schema.json
slug: application-discovery-service-agent-configuration-status
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: AgentConfigurationStatus
---
