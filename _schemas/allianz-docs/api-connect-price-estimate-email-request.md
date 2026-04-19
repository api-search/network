---
description: Request body for emailing a price estimate to a customer
layout: schema
name: PriceEstimateEmailRequest
properties_list:
- description: Unique identifier of the price estimate to email
  name: estimate_id
  type: string
- description: Customer email address to send the estimate to
  name: customer_email
  type: string
- description: Customer full name for personalizing the email
  name: customer_name
  type: string
provider_name: Allianz
provider_slug: allianz-docs
schema_file: json-schema/api-connect-price-estimate-email-request-schema.json
slug: api-connect-price-estimate-email-request
tags:
- Financial Services
- Insurance
- Asset Management
title: PriceEstimateEmailRequest
---
