---
description: A saved collection of series requests that can be executed as an order for bulk data retrieval.
layout: schema
name: Basket
properties_list:
- description: Unique identifier for the basket.
  name: basketId
  type: string
- description: User-defined name for the basket.
  name: name
  type: string
- description: Optional description of the basket contents and purpose.
  name: description
  type: string
- description: The series requests contained in the basket.
  name: series
  type: array
- description: When the basket was created.
  name: createdAt
  type: string
- description: When the basket was last modified.
  name: updatedAt
  type: string
provider_name: Moody's
provider_slug: moodys
schema_file: json-schema/moodys-data-buffet-basket-schema.json
slug: moodys-data-buffet-basket
tags:
- Climate Risk
- Compliance
- Credit Risk
- Economic Data
- Entity Verification
- Financial Analytics
- Insurance
- KYC
- Risk
- Screening
title: Basket
---
