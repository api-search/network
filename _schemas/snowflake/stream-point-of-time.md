---
description: ''
layout: schema
name: PointOfTime
properties_list:
- description: 'Type of the point of time. Possible values include: timestamp, offset, statement'
  name: point_of_time_type
  type: string
- description: Relation to the point of time. Currently, the API supports `at` and `before`
  name: reference
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/stream-point-of-time-schema.json
slug: stream-point-of-time
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: PointOfTime
---
