---
description: PaymentMethodResponse schema from Adyen API
layout: schema
name: PaymentMethodResponse
properties_list:
- description: Pagination references.
  name: _links
  type: object
- description: The list of supported payment methods and their details.
  name: data
  type: array
- description: Total number of items.
  name: itemsTotal
  type: integer
- description: Total number of pages.
  name: pagesTotal
  type: integer
- description: Payment method types with errors.
  name: typesWithErrors
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-payment-method-response-schema.json
slug: management-payment-method-response
tags:
- Payments
- Financial Services
- Fintech
title: PaymentMethodResponse
---
