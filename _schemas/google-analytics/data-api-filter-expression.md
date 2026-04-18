---
description: To express dimension or metric filters. The fields in the same FilterExpression need to be either all dimensions or all metrics.
layout: schema
name: FilterExpression
properties_list:
- description: A list of filter expressions.
  name: andGroup
  type: object
- description: An expression to filter dimension or metric values.
  name: filter
  type: object
- description: To express dimension or metric filters. The fields in the same FilterExpression need to be either all dimensions or all metrics.
  name: notExpression
  type: object
- description: A list of filter expressions.
  name: orGroup
  type: object
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/data-api-filter-expression-schema.json
slug: data-api-filter-expression
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: FilterExpression
---
