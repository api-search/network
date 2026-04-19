---
description: ConnectorProfile schema from Amazon AppFlow API
layout: schema
name: ConnectorProfile
properties_list:
- description: The Amazon Resource Name (ARN) of the connector profile.
  name: connectorProfileArn
  type: string
- description: The name of the connector profile.
  name: connectorProfileName
  type: string
- description: The type of connector.
  name: connectorType
  type: string
- description: The label of the connector.
  name: connectorLabel
  type: string
- description: Indicates the connection mode and if it is public or private.
  name: connectionMode
  type: string
- description: The Amazon Resource Name (ARN) of the connector profile credentials.
  name: credentialsArn
  type: string
- description: The connector-specific properties of the profile configuration.
  name: connectorProfileProperties
  type: object
- description: Specifies when the connector profile was created.
  name: createdAt
  type: integer
- description: Specifies when the connector profile was last updated.
  name: lastUpdatedAt
  type: integer
- description: Specifies the private connection provisioning state.
  name: privateConnectionProvisioningState
  type: object
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-connector-profile-schema.json
slug: appflow-connector-profile
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: ConnectorProfile
---
