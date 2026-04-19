---
description: ConnectorEntityField schema from Amazon AppFlow API
layout: schema
name: ConnectorEntityField
properties_list:
- description: The unique identifier of the connector field.
  name: identifier
  type: string
- description: The parent identifier of the connector field.
  name: parentIdentifier
  type: string
- description: The label applied to a connector entity field.
  name: label
  type: string
- description: Booelan value that indicates whether this field can be used as a primary key.
  name: isPrimaryKey
  type: boolean
- description: Default value that can be assigned to this field.
  name: defaultValue
  type: string
- description: Booelan value that indicates whether this field is deprecated or not.
  name: isDeprecated
  type: boolean
- description: Contains details regarding the supported FieldType, including the corresponding filterOperators and supportedValues.
  name: supportedFieldTypeDetails
  type: object
- description: A description of the connector entity field.
  name: description
  type: string
- description: The properties that can be applied to a field when the connector is being used as a source.
  name: sourceProperties
  type: object
- description: The properties applied to a field when the connector is being used as a destination.
  name: destinationProperties
  type: object
provider_name: Amazon AppFlow
provider_slug: amazon-appflow
schema_file: json-schema/appflow-connector-entity-field-schema.json
slug: appflow-connector-entity-field
tags:
- AWS
- Connectors
- Data Flow
- Data Integration
- ETL
- Integration
- SaaS
- Data Transfer
title: ConnectorEntityField
---
