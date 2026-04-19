---
description: ConnectorDetail schema from Amazon AppFlow API
layout: schema
name: ConnectorDetail
properties_list:
- description: A description about the registered connector.
  name: connectorDescription
  type: string
- description: The name of the connector.
  name: connectorName
  type: string
- description: The owner of the connector.
  name: connectorOwner
  type: string
- description: The connector version.
  name: connectorVersion
  type: string
- description: The application type of the connector.
  name: applicationType
  type: string
- description: The connector type.
  name: connectorType
  type: string
- description: The label used for registering the connector.
  name: connectorLabel
  type: string
- description: The time at which the connector was registered.
  name: registeredAt
  type: integer
- description: The user who registered the connector.
  name: registeredBy
  type: string
- description: The provisioning type that the connector uses.
  name: connectorProvisioningType
  type: string
- description: ''
  name: connectorModes
  type: array
- description: ''
  name: supportedDataTransferTypes
  type: array
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-connector-detail-schema.json
slug: appflow-connector-detail
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: ConnectorDetail
---
