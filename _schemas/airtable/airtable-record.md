---
description: An Airtable record representing a single row in a table. Records are the fundamental data units in Airtable, containing field values that correspond to the table's column definitions.
layout: schema
name: Airtable Record
properties_list:
- description: The unique identifier for the record. Record IDs always start with the 'rec' prefix.
  name: id
  type: string
- description: The date and time when the record was created, in ISO 8601 format.
  name: createdTime
  type: string
- description: A mapping of field names (or field IDs when returnFieldsByFieldId is enabled) to their cell values. The keys and value types depend on the table's schema definition.
  name: fields
  type: object
provider_name: Airtable
provider_slug: airtable
schema_file: json-schema/airtable-record-schema.json
slug: airtable-record
tags:
- Applications
- Collaboration
- Data
- Databases
- Low-Code
- Productivity
- Spreadsheets
title: Airtable Record
---
