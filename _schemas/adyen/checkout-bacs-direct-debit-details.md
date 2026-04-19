---
description: BacsDirectDebitDetails schema from Adyen API
layout: schema
name: BacsDirectDebitDetails
properties_list:
- description: The bank account number (without separators).
  name: bankAccountNumber
  type: string
- description: The bank routing number of the account.
  name: bankLocationId
  type: string
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The name of the bank account holder.
  name: holderName
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: recurringDetailReference
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: storedPaymentMethodId
  type: string
- description: '**directdebit_GB**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-bacs-direct-debit-details-schema.json
slug: checkout-bacs-direct-debit-details
tags:
- Payments
- Financial Services
- Fintech
title: BacsDirectDebitDetails
---
