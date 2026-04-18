---
description: Developer metadata associated with a location or object in a spreadsheet.
layout: schema
name: DeveloperMetadata
properties_list:
- description: The spreadsheet-scoped unique ID that identifies the metadata.
  name: metadataId
  type: integer
- description: The metadata key.
  name: metadataKey
  type: string
- description: Data associated with the metadata's key.
  name: metadataValue
  type: string
- description: The metadata visibility.
  name: visibility
  type: string
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-developer-metadata-schema.json
slug: google-sheets-developer-metadata
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: DeveloperMetadata
---
