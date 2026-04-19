---
description: ScheduleAccountUpdaterRequest schema from Adyen API
layout: schema
name: ScheduleAccountUpdaterRequest
properties_list:
- description: This field contains additional data, which may be required for a particular request.
  name: additionalData
  type: object
- description: Credit card data. Optional if `shopperReference` and `selectedRecurringDetailReference` are provided.
  name: card
  type: object
- description: Account of the merchant.
  name: merchantAccount
  type: string
- description: A reference that merchants can apply for the call.
  name: reference
  type: string
- description: The selected detail recurring reference. Optional if `card` is provided.
  name: selectedRecurringDetailReference
  type: string
- description: The reference of the shopper that owns the recurring contract. Optional if `card` is provided.
  name: shopperReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/recurring-schedule-account-updater-request-schema.json
slug: recurring-schedule-account-updater-request
tags:
- Payments
- Financial Services
- Fintech
title: ScheduleAccountUpdaterRequest
---
