---
description: Field definition for creating or updating custom fields
layout: schema
name: FieldDefinition
properties_list:
- description: The identifier of the field
  name: fieldName
  type: string
- description: The human-readable name of the field
  name: displayName
  type: string
- description: Optional description of the field
  name: description
  type: string
- description: The data type of the field. Valid values are string, boolean, date, datetime, singleSelect, multiSelect, int, float, reference
  name: valueType
  type: string
- description: Indicates if the field is required
  name: required
  type: boolean
- description: Indicates if the field must be unique across all records
  name: unique
  type: boolean
- description: Indicates if the field should be indexed for faster search
  name: indexed
  type: boolean
- description: ''
  name: stringOptions
  type: object
- description: ''
  name: numericOptions
  type: object
- description: ''
  name: association
  type: object
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-field-definition-schema.json
slug: ampersand-api-field-definition
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: FieldDefinition
---
