---
description: KYCCheckStatusData schema from Adyen API
layout: schema
name: KYCCheckStatusData
properties_list:
- description: A list of the fields required for execution of the check.
  name: requiredFields
  type: array
- description: 'The status of the check. Possible values: **AWAITING_DATA** , **DATA_PROVIDED**, **FAILED**, **INVALID_DATA**, **PASSED**, **PENDING**, **RETRY_LIMIT_REACHED**.'
  name: status
  type: string
- description: A summary of the execution of the check.
  name: summary
  type: object
- description: 'The type of check. Possible values: * **BANK_ACCOUNT_VERIFICATION**: Used in v5 and earlier. Replaced by **PAYOUT_METHOD_VERIFICATION** in v6 and later. * **COMPANY_VERIFICATION** * **CARD_VERIFICATIO'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-kyc-check-status-data-schema.json
slug: accounts-kyc-check-status-data
tags:
- Payments
- Financial Services
- Fintech
title: KYCCheckStatusData
---
