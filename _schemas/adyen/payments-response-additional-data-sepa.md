---
description: ResponseAdditionalDataSepa schema from Adyen API
layout: schema
name: ResponseAdditionalDataSepa
properties_list:
- description: 'The transaction signature date. Format: yyyy-MM-dd'
  name: sepadirectdebit.dateOfSignature
  type: string
- description: Its value corresponds to the pspReference value of the transaction.
  name: sepadirectdebit.mandateId
  type: string
- description: 'This field can take one of the following values: * OneOff: (OOFF) Direct debit instruction to initiate exactly one direct debit transaction. * First: (FRST) Initial/first collection in a series of dir'
  name: sepadirectdebit.sequenceType
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-response-additional-data-sepa-schema.json
slug: payments-response-additional-data-sepa
tags:
- Payments
- Financial Services
- Fintech
title: ResponseAdditionalDataSepa
---
