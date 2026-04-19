---
description: ListConnectorEntitiesRequest schema from Amazon AppFlow API
layout: schema
name: ListConnectorEntitiesRequest
properties_list:
- description: The name of the connector profile. The name is unique for each ConnectorProfile in the AWS account.
  name: connectorProfileName
  type: string
- description: The type of connector, such as Salesforce, Marketo, and so on.
  name: connectorType
  type: string
- description: This optional parameter is specific to connector implementation. Some connectors support multiple levels or categories of entities.
  name: entitiesPath
  type: string
- description: The version of the API that's used by the connector.
  name: apiVersion
  type: string
- description: The maximum number of items that should be returned in the result set.
  name: maxResults
  type: integer
- description: The pagination token for next page of data.
  name: nextToken
  type: string
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-list-connector-entities-request-schema.json
slug: appflow-list-connector-entities-request
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: ListConnectorEntitiesRequest
---
