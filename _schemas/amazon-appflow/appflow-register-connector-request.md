---
description: RegisterConnectorRequest schema from Amazon AppFlow API
layout: schema
name: RegisterConnectorRequest
properties_list:
- description: The name of the connector. The name is unique for each ConnectorRegistration in your Amazon Web Services account.
  name: connectorLabel
  type: string
- description: A description about the connector that's being registered.
  name: description
  type: string
- description: The provisioning type of the connector. Currently the only supported value is LAMBDA.
  name: connectorProvisioningType
  type: string
- description: The provisioning type of the connector.
  name: connectorProvisioningConfig
  type: object
- description: Idempotency token.
  name: clientToken
  type: string
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-register-connector-request-schema.json
slug: appflow-register-connector-request
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: RegisterConnectorRequest
---
