---
description: A single error detail object.
layout: schema
name: Error
properties_list:
- description: A UUID for this particular occurrence of the problem.
  name: id
  type: string
- description: Error status code description.
  name: code
  type: string
- description: The plain text error message.
  name: title
  type: string
- description: The endpoint path for reference.
  name: links
  type: object
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-fundamentals-error-schema.json
slug: factset-fundamentals-error
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: Error
---
