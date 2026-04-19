---
description: NotifyShopperRequest schema from Adyen API
layout: schema
name: NotifyShopperRequest
properties_list:
- description: The amount of the upcoming payment.
  name: amount
  type: object
- description: Date on which the subscription amount will be debited from the shopper. In YYYY-MM-DD format
  name: billingDate
  type: string
- description: Sequence of the debit. Depends on Frequency and Billing Attempts Rule.
  name: billingSequenceNumber
  type: string
- description: Reference of Pre-debit notification that is displayed to the shopper. Optional field. Maps to reference if missing
  name: displayedReference
  type: string
- description: The merchant account identifier with which you want to process the transaction.
  name: merchantAccount
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: recurringDetailReference
  type: string
- description: Pre-debit notification reference sent by the merchant. This is a mandatory field
  name: reference
  type: string
- description: The ID that uniquely identifies the shopper. This `shopperReference` must be the same as the `shopperReference` used in the initial payment.
  name: shopperReference
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: storedPaymentMethodId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/recurring-notify-shopper-request-schema.json
slug: recurring-notify-shopper-request
tags:
- Payments
- Financial Services
- Fintech
title: NotifyShopperRequest
---
