---
description: An Airtable table is a collection of records organized with a defined set of fields and views within a base. Tables define the structure and schema of the data they contain.
layout: schema
name: Airtable Table
properties_list:
- description: The unique identifier for the table. Table IDs always start with the 'tbl' prefix.
  name: id
  type: string
- description: The display name of the table.
  name: name
  type: string
- description: An optional description of the table's purpose and contents.
  name: description
  type:
  - string
  - 'null'
- description: The ID of the primary field for this table. The primary field serves as the main identifier for records.
  name: primaryFieldId
  type: string
- description: The field definitions (columns) in the table.
  name: fields
  type: array
- description: The view definitions in the table.
  name: views
  type: array
provider_name: Airtable
provider_slug: airtable
schema_file: json-schema/airtable-table-schema.json
slug: airtable-table
tags:
- Applications
- Collaboration
- Data
- Databases
- Low-Code
- Productivity
- Spreadsheets
title: Airtable Table
---
