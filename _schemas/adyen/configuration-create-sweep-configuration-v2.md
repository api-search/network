---
description: CreateSweepConfigurationV2 schema from Adyen API
layout: schema
name: CreateSweepConfigurationV2
properties_list:
- description: 'The type of transfer that results from the sweep. Possible values: - **bank**: Sweep to a [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments__resPa'
  name: category
  type: string
- description: The destination or the source of the funds, depending on the sweep `type`. Either a `balanceAccountId`, `transferInstrumentId`, or `merchantAccount` is required.
  name: counterparty
  type: object
- description: The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) in uppercase. For example, **EUR**. The sweep currency must match any of the [balances currencies](
  name: currency
  type: string
- description: The message that will be used in the sweep transfer's description body with a maximum length of 140 characters. If the message is longer after replacing placeholders, the message will be cut off at 14
  name: description
  type: string
- description: 'The list of priorities for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. You can provide multiple priorities. Adyen will try to pay out using '
  name: priorities
  type: array
- description: The reason for disabling the sweep.
  name: reason
  type: string
- description: The schedule when the `triggerAmount` is evaluated. If the balance meets the threshold, funds are pushed out of or pulled in to the balance account.
  name: schedule
  type: object
- description: 'The status of the sweep. If not provided, by default, this is set to **active**. Possible values: * **active**: the sweep is enabled and funds will be pulled in or pushed out based on the defined conf'
  name: status
  type: string
- description: The amount that must be pushed out or pulled in. You can configure either `sweepAmount` or `targetAmount`, not both.
  name: sweepAmount
  type: object
- description: The amount that must be available in the balance account after the sweep. You can configure either `sweepAmount` or `targetAmount`, not both.
  name: targetAmount
  type: object
- description: The threshold amount that triggers the sweep. If not provided, by default, the amount is set to zero. The `triggerAmount` is evaluated according to the specified `schedule.type`. * For `type` **pull**
  name: triggerAmount
  type: object
- description: 'The direction of sweep, whether pushing out or pulling in funds to the balance account. If not provided, by default, this is set to **push**. Possible values: * **push**: _push out funds_ to a destina'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-create-sweep-configuration-v2-schema.json
slug: configuration-create-sweep-configuration-v2
tags:
- Payments
- Financial Services
- Fintech
title: CreateSweepConfigurationV2
---
