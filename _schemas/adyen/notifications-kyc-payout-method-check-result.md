---
description: KYCPayoutMethodCheckResult schema from Adyen API
layout: schema
name: KYCPayoutMethodCheckResult
properties_list:
- description: A list of the checks and their statuses.
  name: checks
  type: array
- description: The unique ID of the payoput method to which the check applies.
  name: payoutMethodCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-kyc-payout-method-check-result-schema.json
slug: notifications-kyc-payout-method-check-result
tags:
- Payments
- Financial Services
- Fintech
title: KYCPayoutMethodCheckResult
---
