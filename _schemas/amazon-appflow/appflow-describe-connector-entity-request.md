---
description: DescribeConnectorEntityRequest schema from Amazon AppFlow API
layout: schema
name: DescribeConnectorEntityRequest
properties_list:
- description: The entity name for that connector.
  name: connectorEntityName
  type: string
- description: The type of connector application, such as Salesforce, Marketo, and so on.
  name: connectorType
  type: string
- description: The name of the connector profile. The name is unique for each ConnectorProfile in the AWS account.
  name: connectorProfileName
  type: string
- description: The version of the API that's used by the connector.
  name: apiVersion
  type: string
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-describe-connector-entity-request-schema.json
slug: appflow-describe-connector-entity-request
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: DescribeConnectorEntityRequest
---
