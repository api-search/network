---
description: A data source table, which allows the user to import a static table of data from the DataSource into Sheets.
layout: schema
name: DataSourceTable
properties_list:
- description: The ID of the data source the data source table is associated with.
  name: dataSourceId
  type: string
- description: The type to select columns for the data source table.
  name: columnSelectionType
  type: string
- description: Columns selected for the data source table.
  name: columns
  type: array
- description: Filter specifications in the data source table.
  name: filterSpecs
  type: array
- description: Sort specifications in the data source table.
  name: sortSpecs
  type: array
- description: The limit of rows to return.
  name: rowLimit
  type: integer
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-data-source-table-schema.json
slug: google-sheets-data-source-table
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: DataSourceTable
---
