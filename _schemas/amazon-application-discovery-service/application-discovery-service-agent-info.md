---
description: AgentInfo schema from Amazon Application Discovery Service API
layout: schema
name: AgentInfo
properties_list:
- description: The agent or collector ID.
  name: agentId
  type: string
- description: The name of the host where the agent or collector resides.
  name: hostName
  type: string
- description: Network details about the host where the agent or collector resides.
  name: agentNetworkInfoList
  type: array
- description: The ID of the connector.
  name: connectorId
  type: string
- description: The agent or collector version.
  name: version
  type: string
- description: The health of the agent or collector.
  name: health
  type: string
- description: Time since agent or collector health was reported.
  name: lastHealthPingTime
  type: string
- description: Status of the collection process for the agent or collector.
  name: collectionStatus
  type: string
- description: Type of agent.
  name: agentType
  type: string
- description: Agent's first registration timestamp in UTC.
  name: registeredTime
  type: string
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-agent-info-schema.json
slug: application-discovery-service-agent-info
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: AgentInfo
---
