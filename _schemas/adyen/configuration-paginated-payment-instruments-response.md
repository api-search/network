---
description: PaginatedPaymentInstrumentsResponse schema from Adyen API
layout: schema
name: PaginatedPaymentInstrumentsResponse
properties_list:
- description: Indicates whether there are more items on the next page.
  name: hasNext
  type: boolean
- description: Indicates whether there are more items on the previous page.
  name: hasPrevious
  type: boolean
- description: List of payment instruments associated with the balance account.
  name: paymentInstruments
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-paginated-payment-instruments-response-schema.json
slug: configuration-paginated-payment-instruments-response
tags:
- Payments
- Financial Services
- Fintech
title: PaginatedPaymentInstrumentsResponse
---
