---
description: RecurringDetailsRequest schema from Adyen API
layout: schema
name: RecurringDetailsRequest
properties_list:
- description: The merchant account identifier you want to process the (transaction) request with.
  name: merchantAccount
  type: string
- description: A container for the type of a recurring contract to be retrieved. The contract value needs to match the contract value submitted in the payment transaction used to create a recurring contract. However
  name: recurring
  type: object
- description: The reference you use to uniquely identify the shopper (e.g. user ID or account ID).
  name: shopperReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/recurring-recurring-details-request-schema.json
slug: recurring-recurring-details-request
tags:
- Payments
- Financial Services
- Fintech
title: RecurringDetailsRequest
---
