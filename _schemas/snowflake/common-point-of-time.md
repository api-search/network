---
description: Point of time.
layout: schema
name: PointOfTime
properties_list:
- description: 'Type of the point of time. Possible values include: - `timestamp`: Exact time using the standard timezone format. Example: `2023-09-15 10:59:43`. - `offset`: Interval relative to ''now.'' Example: `1 da'
  name: point_of_time_type
  type: string
- description: Relation to the point of time. Currently, the API supports `at` and `before`.
  name: reference
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/common-point-of-time-schema.json
slug: common-point-of-time
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: PointOfTime
---
