---
description: DescribeConnectorProfilesRequest schema from Amazon AppFlow API
layout: schema
name: DescribeConnectorProfilesRequest
properties_list:
- description: The name of the connector profile. The name is unique for each ConnectorProfile in the AWS account.
  name: connectorProfileNames
  type: array
- description: The type of connector, such as Salesforce, Marketo, and so on.
  name: connectorType
  type: string
- description: The name of the connector.
  name: connectorLabel
  type: string
- description: Specifies the maximum number of items that should be returned in the result set. The default for maxResults is 20.
  name: maxResults
  type: integer
- description: The pagination token for next page of data.
  name: nextToken
  type: string
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-describe-connector-profiles-request-schema.json
slug: appflow-describe-connector-profiles-request
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: DescribeConnectorProfilesRequest
---
