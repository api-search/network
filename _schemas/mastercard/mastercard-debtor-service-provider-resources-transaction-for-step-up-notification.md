---
description: ''
layout: schema
name: TransactionForStepUpNotification
properties_list:
- description: Unique identifier assigned by Mastercard, to identify the payment request in subsequent transactions or services.
  name: paymentRequestLifecycleId
  type: string
- description: Text message that DSP will be providing to display to the Debtor on Creditor website or application.
  name: stepUpMessage
  type: string
- description: URL that will be used by the Debtor to open the banking app from Creditor's website or application on a single device journey. Creditor should only use this when it's a single device journey.
  name: applicationUrl
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-debtor-service-provider-resources-transaction-for-step-up-notification-schema.json
slug: mastercard-debtor-service-provider-resources-transaction-for-step-up-notification
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: TransactionForStepUpNotification
---
