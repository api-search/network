---
consumed_apis:
- excel-graph
description: Workflow capability for automating Excel spreadsheet operations including worksheet management, data manipulation, table operations, and chart generation via Microsoft Graph.
layout: capability
name: Microsoft Excel Spreadsheet Automation
operations:
- description: List all worksheets.
  method: GET
  name: list-worksheets
  path: /v1/worksheets
- description: Create a new worksheet.
  method: POST
  name: create-worksheet
  path: /v1/worksheets
- description: List rows in a table.
  method: GET
  name: list-table-rows
  path: /v1/tables/{table-id}/rows
- description: Add a row to a table.
  method: POST
  name: add-table-row
  path: /v1/tables/{table-id}/rows
- description: Get a cell range.
  method: GET
  name: get-range
  path: /v1/ranges
- description: List charts.
  method: GET
  name: list-charts
  path: /v1/charts
personas: []
provider_name: Microsoft Excel
provider_slug: microsoft-excel
search_terms:
- spreadsheet automation
- data management
- microsoft
- microsoft excel
- get a cell range.
- update cell values in a specified range.
- update range
- list all worksheets in the workbook.
- read cell values from a specified range.
- automation
- manage worksheets.
- spreadsheets
- create worksheet
- create a new worksheet in the workbook.
- office
- list all worksheets.
- list all charts in a worksheet.
- Data Analyst
- Business Analyst
- list worksheets
- list table rows
- cell range operations.
- add a row to a table.
- get range
- business users automating excel-based reporting.
- microsoft 365
- list rows in a table.
- analysts working with excel workbooks for data processing.
- manage table rows.
- add table row
- list charts.
- data analysis
- list all rows in an excel table.
- list charts
- chart operations.
- create a new worksheet.
- add a new data row to an excel table.
- automate excel workbook operations.
slug: spreadsheet-automation
tags:
- Microsoft Excel
- Spreadsheet Automation
- Data Management
tools:
- description: List all worksheets in the workbook.
  hints:
    openWorld: true
    readOnly: true
  name: list-worksheets
- description: Create a new worksheet in the workbook.
  hints:
    readOnly: false
  name: create-worksheet
- description: List all rows in an Excel table.
  hints:
    openWorld: true
    readOnly: true
  name: list-table-rows
- description: Add a new data row to an Excel table.
  hints:
    readOnly: false
  name: add-table-row
- description: Read cell values from a specified range.
  hints:
    openWorld: true
    readOnly: true
  name: get-range
- description: Update cell values in a specified range.
  hints:
    readOnly: false
  name: update-range
- description: List all charts in a worksheet.
  hints:
    openWorld: true
    readOnly: true
  name: list-charts
---
