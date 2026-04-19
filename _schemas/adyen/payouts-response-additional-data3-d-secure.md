---
description: ResponseAdditionalData3DSecure schema from Adyen API
layout: schema
name: ResponseAdditionalData3DSecure
properties_list:
- description: Information provided by the issuer to the cardholder. If this field is present, you need to display this information to the cardholder.
  name: cardHolderInfo
  type: string
- description: The Cardholder Authentication Verification Value (CAVV) for the 3D Secure authentication session, as a Base64-encoded 20-byte array.
  name: cavv
  type: string
- description: The CAVV algorithm used.
  name: cavvAlgorithm
  type: string
- description: Shows the [exemption type](https://docs.adyen.com/payments-fundamentals/psd2-sca-compliance-and-implementation-guide#specifypreferenceinyourapirequest) that Adyen requested for the payment. Possible v
  name: scaExemptionRequested
  type: string
- description: Indicates whether a card is enrolled for 3D Secure 2.
  name: threeds2.cardEnrolled
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payouts-response-additional-data3-d-secure-schema.json
slug: payouts-response-additional-data3-d-secure
tags:
- Payments
- Financial Services
- Fintech
title: ResponseAdditionalData3DSecure
---
