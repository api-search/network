---
description: AccountPayoutState schema from Adyen API
layout: schema
name: AccountPayoutState
properties_list:
- description: Indicates whether payouts are allowed. This field is the overarching payout status, and is the aggregate of multiple conditions (e.g., KYC status, disabled flag, etc). If this field is false, no payou
  name: allowPayout
  type: boolean
- description: The reason why payouts (to all of the account holder's accounts) have been disabled (by the platform). If the `disabled` field is true, this field can be used to explain why.
  name: disableReason
  type: string
- description: Indicates whether payouts have been disabled (by the platform) for all of the account holder's accounts. A platform may enable and disable this field at their discretion. If this field is true, `allow
  name: disabled
  type: boolean
- description: The reason why payouts (to all of the account holder's accounts) have been disabled (by Adyen). If payouts have been disabled by Adyen, this field will explain why. If this field is blank, payouts hav
  name: notAllowedReason
  type: string
- description: The maximum amount that payouts are limited to. Only applies if payouts are allowed but limited.
  name: payoutLimit
  type: object
- description: The payout tier that the account holder occupies.
  name: tierNumber
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-account-payout-state-schema.json
slug: accounts-account-payout-state
tags:
- Payments
- Financial Services
- Fintech
title: AccountPayoutState
---
