---
description: AccountHolderVerificationNotificationContent schema from Adyen API
layout: schema
name: AccountHolderVerificationNotificationContent
properties_list:
- description: The code of the account holder.
  name: accountHolderCode
  type: string
- description: Information on the verification status
  name: kycCheckStatusData
  type: object
- description: The unique ID of the legal arrangement that has been verified.
  name: legalArrangementCode
  type: string
- description: The unique ID of the legal arrangement entity that has been verified.
  name: legalArrangementEntityCode
  type: string
- description: The unique code of the payout method that has been verified.
  name: payoutMethodCode
  type: string
- description: The code of the shareholder that has been verified.
  name: shareholderCode
  type: string
- description: The code of the signatory that has been verified.
  name: signatoryCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-account-holder-verification-notification-content-schema.json
slug: notifications-account-holder-verification-notification-content
tags:
- Payments
- Financial Services
- Fintech
title: AccountHolderVerificationNotificationContent
---
