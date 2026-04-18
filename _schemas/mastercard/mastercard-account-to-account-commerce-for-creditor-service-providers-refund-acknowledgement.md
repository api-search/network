---
description: ''
layout: schema
name: RefundAcknowledgement
properties_list:
- description: Unique identifier assigned by Mastercard, to identify the refund request in subsequent transactions or services.
  name: refundRequestLifecycleId
  type: string
- description: Refund Status returned to Mastercard. * Refer to Codes and Formats section for more details.
  name: refundRequestStatus
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-account-to-account-commerce-for-creditor-service-providers-refund-acknowledgement-schema.json
slug: mastercard-account-to-account-commerce-for-creditor-service-providers-refund-acknowledgement
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: RefundAcknowledgement
---
