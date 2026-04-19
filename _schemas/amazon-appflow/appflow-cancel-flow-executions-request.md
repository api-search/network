---
description: CancelFlowExecutionsRequest schema from Amazon AppFlow API
layout: schema
name: CancelFlowExecutionsRequest
properties_list:
- description: The name of a flow with active runs that you want to cancel.
  name: flowName
  type: string
- description: The ID of each active run to cancel. If you omit this parameter, your request ends all active runs that belong to the flow.
  name: executionIds
  type: array
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-cancel-flow-executions-request-schema.json
slug: appflow-cancel-flow-executions-request
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: CancelFlowExecutionsRequest
---
