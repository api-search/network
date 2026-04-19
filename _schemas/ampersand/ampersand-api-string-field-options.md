---
description: Additional options for string fields
layout: schema
name: StringFieldOptions
properties_list:
- description: Maximum length of the string field
  name: length
  type: integer
- description: Regex pattern that the string field value must match
  name: pattern
  type: string
- description: List of allowed values for enum fields
  name: values
  type: array
- description: Indicates if the field value must be limited to what's in Values
  name: valuesRestricted
  type: boolean
- description: Default value for the field
  name: defaultValue
  type: string
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-string-field-options-schema.json
slug: ampersand-api-string-field-options
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: StringFieldOptions
---
