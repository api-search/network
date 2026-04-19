---
description: Filters securities based on asset classes and other fields depending on the asset classes.
layout: schema
name: include_exclude_object
properties_list:
- description: String containing the field name to filter on. Each asset class has its own set of field (i.e. equity_type, is_primary, region,etc)
  name: field
  type: string
- description: String containing the asset class for the filter to be applied on. If not included or left empty, it will apply the filter against all asset classes
  name: entity
  type: string
- description: Values you wish to filter on, as a comma-separated list. The values within this list are tied by an OR operation.
  name: values
  type: array
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-id-lookup-include_exclude_object-schema.json
slug: factset-id-lookup-include_exclude_object
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: include_exclude_object
---
