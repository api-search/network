---
description: CreateConnectorProfileRequest schema from Amazon AppFlow API
layout: schema
name: CreateConnectorProfileRequest
properties_list:
- description: The name of the connector profile. The name is unique for each ConnectorProfile in your AWS account.
  name: connectorProfileName
  type: string
- description: Idempotency token.
  name: clientToken
  type: string
- description: The type of connector, such as Salesforce, Marketo, and so on.
  name: connectorType
  type: string
- description: The label of the connector. The label is unique for each ConnectorRegistration in your AWS account.
  name: connectorLabel
  type: string
- description: Indicates the connection mode and specifies whether it is public or private.
  name: connectionMode
  type: string
- description: The ARN of the KMS key to use to encrypt your connector profile credentials.
  name: kmsArn
  type: string
- description: Defines the connector-specific configuration and credentials.
  name: connectorProfileConfig
  type: object
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-create-connector-profile-request-schema.json
slug: appflow-create-connector-profile-request
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: CreateConnectorProfileRequest
---
