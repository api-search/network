---
consumed_apis:
- google-sheets
description: Workflow for managing spreadsheet data including creating spreadsheets, reading and writing cell values, batch operations, and metadata management. Used by data analysts, developers, and automation engineers.
layout: capability
name: Google Sheets Spreadsheet Data Management
operations:
- description: Create a new spreadsheet
  method: POST
  name: create-spreadsheet
  path: /v1/spreadsheets
- description: Get spreadsheet details
  method: GET
  name: get-spreadsheet
  path: /v1/spreadsheets/{spreadsheetId}
- description: Read values from a range
  method: GET
  name: get-values
  path: /v1/spreadsheets/{spreadsheetId}/values/{range}
- description: Write values to a range
  method: PUT
  name: update-values
  path: /v1/spreadsheets/{spreadsheetId}/values/{range}
- description: Append values to a range
  method: POST
  name: append-values
  path: /v1/spreadsheets/{spreadsheetId}/values/{range}
- description: Clear values from a range
  method: DELETE
  name: clear-values
  path: /v1/spreadsheets/{spreadsheetId}/values/{range}
personas: []
provider_name: Google Sheets
provider_slug: google-sheets
search_terms:
- get spreadsheet details
- get values
- batch update spreadsheet
- get developer metadata by id
- get developer metadata
- write values to a spreadsheet range
- spreadsheet lifecycle operations
- batch update values
- create a new google sheets spreadsheet
- cell value read and write operations
- productivity
- copy a sheet to another spreadsheet
- batch clear values
- create spreadsheet
- clear values from a range
- update values
- read values from multiple ranges at once
- get spreadsheet details by id
- write values to multiple ranges at once
- clear values from multiple ranges
- google sheets
- single spreadsheet operations
- spreadsheets
- search developer metadata
- get spreadsheet
- create a new spreadsheet
- read values from a range
- google workspace
- clear values
- apply batch updates to a spreadsheet
- read values from a spreadsheet range
- clear values from a spreadsheet range
- copy sheet
- batch get values
- append values
- append values to a range
- data management
- append rows of data to a spreadsheet
- search developer metadata matching filters
- automation
- write values to a range
slug: spreadsheet-data-management
tags:
- Google Sheets
- Spreadsheets
- Data Management
- Automation
tools:
- description: Create a new Google Sheets spreadsheet
  hints:
    idempotent: false
    readOnly: false
  name: create-spreadsheet
- description: Get spreadsheet details by ID
  hints:
    idempotent: true
    readOnly: true
  name: get-spreadsheet
- description: Apply batch updates to a spreadsheet
  hints:
    idempotent: false
    readOnly: false
  name: batch-update-spreadsheet
- description: Read values from a spreadsheet range
  hints:
    idempotent: true
    readOnly: true
  name: get-values
- description: Write values to a spreadsheet range
  hints:
    idempotent: true
    readOnly: false
  name: update-values
- description: Append rows of data to a spreadsheet
  hints:
    idempotent: false
    readOnly: false
  name: append-values
- description: Clear values from a spreadsheet range
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: clear-values
- description: Read values from multiple ranges at once
  hints:
    idempotent: true
    readOnly: true
  name: batch-get-values
- description: Write values to multiple ranges at once
  hints:
    idempotent: true
    readOnly: false
  name: batch-update-values
- description: Clear values from multiple ranges
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: batch-clear-values
- description: Copy a sheet to another spreadsheet
  hints:
    idempotent: false
    readOnly: false
  name: copy-sheet
- description: Get developer metadata by ID
  hints:
    idempotent: true
    readOnly: true
  name: get-developer-metadata
- description: Search developer metadata matching filters
  hints:
    idempotent: true
    readOnly: true
  name: search-developer-metadata
---
