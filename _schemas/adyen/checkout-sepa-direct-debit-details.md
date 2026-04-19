---
description: SepaDirectDebitDetails schema from Adyen API
layout: schema
name: SepaDirectDebitDetails
properties_list:
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The International Bank Account Number (IBAN).
  name: iban
  type: string
- description: The name of the bank account holder.
  name: ownerName
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: recurringDetailReference
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: storedPaymentMethodId
  type: string
- description: '**sepadirectdebit**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-sepa-direct-debit-details-schema.json
slug: checkout-sepa-direct-debit-details
tags:
- Payments
- Financial Services
- Fintech
title: SepaDirectDebitDetails
---
