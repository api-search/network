---
description: Request body for creating or updating a basket.
layout: schema
name: BasketCreate
properties_list:
- description: User-defined name for the basket.
  name: name
  type: string
- description: Optional description of the basket.
  name: description
  type: string
- description: The series requests to include in the basket.
  name: series
  type: array
provider_name: Moody's
provider_slug: moodys
schema_file: json-schema/moodys-data-buffet-basket-create-schema.json
slug: moodys-data-buffet-basket-create
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
title: BasketCreate
---
