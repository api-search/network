---
description: UpdateConnectorRegistrationRequest schema from Amazon AppFlow API
layout: schema
name: UpdateConnectorRegistrationRequest
properties_list:
- description: The name of the connector. The name is unique for each ConnectorRegistration in your Amazon Web Services account.
  name: connectorLabel
  type: string
- description: A description about the update that you're making to the connector.
  name: description
  type: string
- description: The provisioning type of the connector.
  name: connectorProvisioningConfig
  type: object
- description: Idempotency token.
  name: clientToken
  type: string
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-update-connector-registration-request-schema.json
slug: appflow-update-connector-registration-request
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: UpdateConnectorRegistrationRequest
---
