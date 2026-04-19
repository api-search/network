---
description: Task schema from Amazon AppFlow API
layout: schema
name: Task
properties_list:
- description: The source fields to which a particular task is applied.
  name: sourceFields
  type: array
- description: The operation to be performed on the provided source fields.
  name: connectorOperator
  type: object
- description: A field in a destination connector, or a field value against which Amazon AppFlow validates a source field.
  name: destinationField
  type: string
- description: Specifies the particular task implementation that Amazon AppFlow performs.
  name: taskType
  type: string
- description: A map used to store task-related information.
  name: taskProperties
  type: object
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-task-schema.json
slug: appflow-task
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: Task
---
