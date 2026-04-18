---
description: Response to a successful YouTube Analytics query request containing the requested report data including column headers and rows of data.
layout: schema
name: QueryResponse
properties_list:
- description: Identifies the API resource's type. Value is youtubeAnalytics#resultTable.
  name: kind
  type: string
- description: A list of objects that describe the columns in the report table. Each object in the list identifies a query dimension or metric and provides information about the data type of that dimension or metric
  name: columnHeaders
  type: array
- description: The list contains all rows of the result table. Each item in the list is an array that contains comma-delimited data corresponding to a single row of data. The order of the comma-delimited data fields
  name: rows
  type: array
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-analytics-query-response-schema.json
slug: youtube-analytics-query-response
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: QueryResponse
---
