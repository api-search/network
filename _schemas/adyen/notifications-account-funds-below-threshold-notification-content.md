---
description: AccountFundsBelowThresholdNotificationContent schema from Adyen API
layout: schema
name: AccountFundsBelowThresholdNotificationContent
properties_list:
- description: The code of the account with funds under threshold
  name: accountCode
  type: string
- description: The date of the funds were found to be below threshold.
  name: balanceDate
  type: object
- description: The current funds in the liable account.
  name: currentFunds
  type: object
- description: The configured fund threshold for the liable account
  name: fundThreshold
  type: object
- description: The code of the merchant account.
  name: merchantAccountCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-account-funds-below-threshold-notification-content-schema.json
slug: notifications-account-funds-below-threshold-notification-content
tags:
- Payments
- Financial Services
- Fintech
title: AccountFundsBelowThresholdNotificationContent
---
