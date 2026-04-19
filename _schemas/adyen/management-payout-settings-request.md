---
description: PayoutSettingsRequest schema from Adyen API
layout: schema
name: PayoutSettingsRequest
properties_list:
- description: 'Indicates if payouts to this bank account are enabled. Default: **true**. To receive payouts into this bank account, both `enabled` and `allowed` must be **true**.'
  name: enabled
  type: boolean
- description: 'The date when Adyen starts paying out to this bank account. Format: [ISO 8601](https://www.w3.org/TR/NOTE-datetime), for example, **2019-11-23T12:25:28Z** or **2020-05-27T20:25:28+08:00**. If not spec'
  name: enabledFromDate
  type: string
- description: The unique identifier of the [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments) that contains the details of the bank account.
  name: transferInstrumentId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-payout-settings-request-schema.json
slug: management-payout-settings-request
tags:
- Payments
- Financial Services
- Fintech
title: PayoutSettingsRequest
---
