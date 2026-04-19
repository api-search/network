---
description: SourceFlowConfig schema from Amazon AppFlow API
layout: schema
name: SourceFlowConfig
properties_list:
- description: The type of connector used as a source.
  name: connectorType
  type: string
- description: The API version of the connector used in the source.
  name: apiVersion
  type: string
- description: The name of the connector profile. Required for all connectors except Amplitude, Datadog, Dynatrace, GoogleAnalytics, Marketo, SAPOData, Salesforce, ServiceNow, Singular, Slack, Trendmicro, and Veeva.
  name: connectorProfileName
  type: string
- description: Specifies the information that is required to query a particular source connector.
  name: sourceConnectorProperties
  type: object
- description: Defines the configuration for a scheduled incremental data pull. If a valid configuration is provided, the fields specified in the configuration are used when querying for the incremental data pull.
  name: incrementalPullConfig
  type: object
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-source-flow-config-schema.json
slug: appflow-source-flow-config
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: SourceFlowConfig
---
