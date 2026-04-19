---
description: DestinationFlowConfig schema from Amazon AppFlow API
layout: schema
name: DestinationFlowConfig
properties_list:
- description: The type of connector used as a destination.
  name: connectorType
  type: string
- description: The API version that the destination connector uses.
  name: apiVersion
  type: string
- description: The name of the connector profile.
  name: connectorProfileName
  type: string
- description: This stores the information that is required to query a particular connector.
  name: destinationConnectorProperties
  type: object
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-destination-flow-config-schema.json
slug: appflow-destination-flow-config
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: DestinationFlowConfig
---
