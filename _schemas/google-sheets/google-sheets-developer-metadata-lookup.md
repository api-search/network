---
description: Selects DeveloperMetadata that matches all of the specified fields.
layout: schema
name: DeveloperMetadataLookup
properties_list:
- description: Limits the selected developer metadata to that which has a matching location type.
  name: locationType
  type: string
- description: Determines how this lookup matches the location.
  name: locationMatchingStrategy
  type: string
- description: Limits the selected developer metadata to that which has a matching metadata ID.
  name: metadataId
  type: integer
- description: Limits the selected developer metadata to that which has a matching metadata key.
  name: metadataKey
  type: string
- description: Limits the selected developer metadata to that which has a matching metadata value.
  name: metadataValue
  type: string
- description: Limits the selected developer metadata to that which has a matching visibility.
  name: visibility
  type: string
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-developer-metadata-lookup-schema.json
slug: google-sheets-developer-metadata-lookup
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: DeveloperMetadataLookup
---
