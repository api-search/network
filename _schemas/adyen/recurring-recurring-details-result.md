---
description: RecurringDetailsResult schema from Adyen API
layout: schema
name: RecurringDetailsResult
properties_list:
- description: The date when the recurring details were created.
  name: creationDate
  type: string
- description: Payment details stored for recurring payments.
  name: details
  type: array
- description: The most recent email for this shopper (if available).
  name: lastKnownShopperEmail
  type: string
- description: The reference you use to uniquely identify the shopper (e.g. user ID or account ID).
  name: shopperReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/recurring-recurring-details-result-schema.json
slug: recurring-recurring-details-result
tags:
- Payments
- Financial Services
- Fintech
title: RecurringDetailsResult
---
