---
description: Order bys define how rows will be sorted in the response. For example, ordering rows by descending event count is one ordering, and ordering rows by the event name string is a different ordering.
layout: schema
name: OrderBy
properties_list:
- description: If true, sorts by descending order.
  name: desc
  type: boolean
- description: Sorts by dimension values.
  name: dimension
  type: object
- description: Sorts by metric values.
  name: metric
  type: object
- description: Sorts by a pivot column group.
  name: pivot
  type: object
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/data-api-order-by-schema.json
slug: data-api-order-by
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: OrderBy
---
