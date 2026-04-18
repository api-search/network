---
description: Dimensions are attributes of your data. For example, the dimension city indicates the city from which an event originates. Dimension values in report responses are strings; for example, the city could be "Paris" or "New York". Requests are allowed up to 9 dimensions.
layout: schema
name: Dimension
properties_list:
- description: 'Used to express a dimension which is the result of a formula of multiple dimensions. Example usages: 1) lower_case(dimension) 2) concatenate(dimension1, symbol, dimension2).'
  name: dimensionExpression
  type: object
- description: The name of the dimension. See the [API Dimensions](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#dimensions) for the list of dimension names supported by core reporti
  name: name
  type: string
provider_name: Google Analytics
provider_slug: google-analytics
schema_file: json-schema/data-api-dimension-schema.json
slug: data-api-dimension
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
title: Dimension
---
