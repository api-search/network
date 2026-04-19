---
description: Request parameters for segment data.
layout: schema
name: SegmentsRequestBody
properties_list:
- description: Segment metric. SALES, OPINC, ASSETS, DEP, or CAPEX.
  name: metrics
  type: string
- description: Segment type. BUS = Business, GEO = Geographic.
  name: segmentType
  type: string
- description: Segment periodicity. ANN or ANN_R only.
  name: periodicity
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-fundamentals-segments-request-body-schema.json
slug: factset-fundamentals-segments-request-body
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: SegmentsRequestBody
---
