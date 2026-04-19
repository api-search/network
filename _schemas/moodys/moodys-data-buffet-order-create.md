---
description: Request body for creating a new order.
layout: schema
name: OrderCreate
properties_list:
- description: The basket to generate the order from.
  name: basketId
  type: string
- description: The desired output file format. Use the /filetypes endpoint to retrieve supported formats.
  name: fileType
  type: string
provider_name: Moody's
provider_slug: moodys
schema_file: json-schema/moodys-data-buffet-order-create-schema.json
slug: moodys-data-buffet-order-create
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
title: OrderCreate
---
