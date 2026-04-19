---
description: UnregisterConnectorRequest schema from Amazon AppFlow API
layout: schema
name: UnregisterConnectorRequest
properties_list:
- description: The label of the connector. The label is unique for each ConnectorRegistration in your Amazon Web Services account.
  name: connectorLabel
  type: string
- description: Indicates whether Amazon AppFlow should unregister the connector, even if it is currently in use in one or more connector profiles.
  name: forceDelete
  type: boolean
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-unregister-connector-request-schema.json
slug: appflow-unregister-connector-request
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: UnregisterConnectorRequest
---
