---
description: An Airtable field represents a column in a table, defining the data type, validation rules, and display configuration for values stored in that column.
layout: schema
name: Airtable Field
properties_list:
- description: The unique identifier for the field. Field IDs always start with the 'fld' prefix.
  name: id
  type: string
- description: The display name of the field.
  name: name
  type: string
- description: The data type of the field, which determines what values can be stored and how they are displayed.
  name: type
  type: string
- description: An optional description of the field.
  name: description
  type:
  - string
  - 'null'
- description: Configuration options specific to the field type. For example, singleSelect fields have a choices array, number fields have a precision setting, and linked record fields specify the linked table.
  name: options
  type: object
provider_name: Airtable
provider_slug: airtable
schema_file: json-schema/airtable-field-schema.json
slug: airtable-field
tags:
- Applications
- Collaboration
- Data
- Databases
- Low-Code
- Productivity
- Spreadsheets
title: Airtable Field
---
