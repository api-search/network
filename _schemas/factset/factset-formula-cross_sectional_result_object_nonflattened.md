---
description: An object returning the results for a single formula.
layout: schema
name: cross_sectional_result_object_nonflattened
properties_list:
- description: If `universe` is submitted instead of `ids`, then the universe attribute will display the universe expression requested.
  name: universe
  type: string
- description: Name of data item (requestId, requested Screening formula, or fsymId)
  name: dataItemName
  type: string
- description: Display Name.
  name: displayName
  type: string
- description: ''
  name: result
  type: array
- description: Data type of the data item
  name: dataType
  type: string
- description: Data item error indicator. * Zero success * Non-zero failure
  name: error
  type: integer
- description: If error is non-zero, errorMessage will display the Screening formula error.
  name: errorMessage
  type: string
- description: Screening formula warnings. This attribute is only displayed if warnings are generated in the execution of the Screening formula.
  name: warnings
  type: array
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-formula-cross_sectional_result_object_nonflattened-schema.json
slug: factset-formula-cross_sectional_result_object_nonflattened
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: cross_sectional_result_object_nonflattened
---
