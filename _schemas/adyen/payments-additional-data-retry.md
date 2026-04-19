---
description: AdditionalDataRetry schema from Adyen API
layout: schema
name: AdditionalDataRetry
properties_list:
- description: The number of times the transaction (not order) has been retried between different payment service providers. For instance, the `chainAttemptNumber` set to 2 means that this transaction has been recen
  name: retry.chainAttemptNumber
  type: string
- description: The index of the attempt to bill a particular order, which is identified by the `merchantOrderReference` field. For example, if a recurring transaction fails and is retried one day later, then the ord
  name: retry.orderAttemptNumber
  type: string
- description: 'The Boolean value indicating whether Adyen should skip or retry this transaction, if possible. > If you submit `retry.chainAttemptNumber`, `retry.orderAttemptNumber`, and `retry.skipRetry` values, we '
  name: retry.skipRetry
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-additional-data-retry-schema.json
slug: payments-additional-data-retry
tags:
- Payments
- Financial Services
- Fintech
title: AdditionalDataRetry
---
