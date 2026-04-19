---
description: PayoutSettings schema from Adyen API
layout: schema
name: PayoutSettings
properties_list:
- description: 'Indicates if payouts to the bank account are allowed. This value is set automatically based on the status of the verification process. The value is: * **true** if `verificationStatus` is **valid**. * '
  name: allowed
  type: boolean
- description: 'Indicates if payouts to this bank account are enabled. Default: **true**. To receive payouts into this bank account, both `enabled` and `allowed` must be **true**.'
  name: enabled
  type: boolean
- description: 'The date when Adyen starts paying out to this bank account. Format: [ISO 8601](https://www.w3.org/TR/NOTE-datetime), for example, **2019-11-23T12:25:28Z** or **2020-05-27T20:25:28+08:00**. If not spec'
  name: enabledFromDate
  type: string
- description: The unique identifier of the payout setting.
  name: id
  type: string
- description: Determines how long it takes for the funds to reach the bank account. Adyen pays out based on the [payout frequency](https://docs.adyen.com/account/getting-paid#payout-frequency). Depending on the cur
  name: priority
  type: string
- description: The unique identifier of the [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments) that contains the details of the bank account.
  name: transferInstrumentId
  type: string
- description: 'The status of the verification process for the bank account. Possible values: * **valid**: the verification was successful. * **pending**: the verification is in progress. * **invalid**: the informati'
  name: verificationStatus
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-payout-settings-schema.json
slug: management-payout-settings
tags:
- Payments
- Financial Services
- Fintech
title: PayoutSettings
---
