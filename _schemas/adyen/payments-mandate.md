---
description: Mandate schema from Adyen API
layout: schema
name: Mandate
properties_list:
- description: The billing amount (in minor units) of the recurring transactions.
  name: amount
  type: string
- description: 'The limitation rule of the billing amount. Possible values: * **max**: The transaction amount can not exceed the `amount`. * **exact**: The transaction amount should be the same as the `amount`.'
  name: amountRule
  type: string
- description: 'The rule to specify the period, within which the recurring debit can happen, relative to the mandate recurring date. Possible values: * **on**: On a specific date. * **before**: Before and on a specif'
  name: billingAttemptsRule
  type: string
- description: 'The number of the day, on which the recurring debit can happen. Should be within the same calendar month as the mandate recurring date. Possible values: 1-31 based on the `frequency`.'
  name: billingDay
  type: string
- description: End date of the billing plan, in YYYY-MM-DD format.
  name: endsAt
  type: string
- description: 'The frequency with which a shopper should be charged. Possible values: **daily**, **weekly**, **biWeekly**, **monthly**, **quarterly**, **halfYearly**, **yearly**.'
  name: frequency
  type: string
- description: The message shown by UPI to the shopper on the approval screen.
  name: remarks
  type: string
- description: Start date of the billing plan, in YYYY-MM-DD format. By default, the transaction date.
  name: startsAt
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-mandate-schema.json
slug: payments-mandate
tags:
- Payments
- Financial Services
- Fintech
title: Mandate
---
