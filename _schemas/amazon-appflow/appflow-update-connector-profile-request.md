---
description: UpdateConnectorProfileRequest schema from Amazon AppFlow API
layout: schema
name: UpdateConnectorProfileRequest
properties_list:
- description: The name of the connector profile and is unique for each ConnectorProfile in the AWS account.
  name: connectorProfileName
  type: string
- description: Idempotency token.
  name: clientToken
  type: string
- description: Indicates the connection mode and if it is public or private.
  name: connectionMode
  type: string
- description: Defines the connector-specific profile configuration and credentials.
  name: connectorProfileConfig
  type: object
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-update-connector-profile-request-schema.json
slug: appflow-update-connector-profile-request
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: UpdateConnectorProfileRequest
---
