---
description: CustomerConnectorInfo schema from Amazon Application Discovery Service API
layout: schema
name: CustomerConnectorInfo
properties_list:
- description: Number of active discovery connectors.
  name: activeConnectors
  type: integer
- description: Number of healthy discovery connectors.
  name: healthyConnectors
  type: integer
- description: Number of blacklisted discovery connectors.
  name: blackListedConnectors
  type: integer
- description: Number of discovery connectors with status SHUTDOWN.
  name: shutdownConnectors
  type: integer
- description: Number of unhealthy discovery connectors.
  name: unhealthyConnectors
  type: integer
- description: Total number of discovery connectors.
  name: totalConnectors
  type: integer
- description: Number of unknown discovery connectors.
  name: unknownConnectors
  type: integer
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-customer-connector-info-schema.json
slug: application-discovery-service-customer-connector-info
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: CustomerConnectorInfo
---
