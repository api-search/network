---
description: The specification of a BigQuery data source that is connected to a sheet.
layout: schema
name: BigQueryDataSourceSpec
properties_list:
- description: The ID of a BigQuery enabled Google Cloud project with a billing account attached.
  name: projectId
  type: string
- description: A BigQueryQuerySpec.
  name: querySpec
  type: object
- description: A BigQueryTableSpec.
  name: tableSpec
  type: object
provider_name: Google Sheets
provider_slug: google-sheets
schema_file: json-schema/google-sheets-big-query-data-source-spec-schema.json
slug: google-sheets-big-query-data-source-spec
tags:
- Google Workspace
- Productivity
- Spreadsheets
title: BigQueryDataSourceSpec
---
