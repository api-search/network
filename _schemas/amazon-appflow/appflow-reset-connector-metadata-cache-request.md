---
description: ResetConnectorMetadataCacheRequest schema from Amazon AppFlow API
layout: schema
name: ResetConnectorMetadataCacheRequest
properties_list:
- description: The name of the connector profile that you want to reset cached metadata for.
  name: connectorProfileName
  type: string
- description: The type of connector to reset cached metadata for.
  name: connectorType
  type: string
- description: Use this parameter if you want to reset cached metadata about the details for an individual entity.
  name: connectorEntityName
  type: string
- description: Use this parameter only if you're resetting the cached metadata about a nested entity.
  name: entitiesPath
  type: string
- description: The API version that you specified in the connector profile that you're resetting cached metadata for.
  name: apiVersion
  type: string
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-reset-connector-metadata-cache-request-schema.json
slug: appflow-reset-connector-metadata-cache-request
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: ResetConnectorMetadataCacheRequest
---
