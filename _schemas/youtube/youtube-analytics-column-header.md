---
description: Describes a single column in an Analytics report response, including its name, type, and data type.
layout: schema
name: ColumnHeader
properties_list:
- description: The name of the dimension or metric.
  name: name
  type: string
- description: The type of the column. Valid values are DIMENSION and METRIC.
  name: columnType
  type: string
- description: The type of data that the column contains. Valid values are STRING, INTEGER, FLOAT, and CURRENCY.
  name: dataType
  type: string
provider_name: Youtube
provider_slug: youtube
schema_file: json-schema/youtube-analytics-column-header-schema.json
slug: youtube-analytics-column-header
tags:
- Google
- Media
- Social
- Streaming
- Video
- Videos
title: ColumnHeader
---
