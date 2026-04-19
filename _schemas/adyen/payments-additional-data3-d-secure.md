---
description: AdditionalData3DSecure schema from Adyen API
layout: schema
name: AdditionalData3DSecure
properties_list:
- description: Indicates if you are able to process 3D Secure 2 transactions natively on your payment page. Send this parameter when you are using `/payments` endpoint with any of our [native 3D Secure 2 solutions](
  name: allow3DS2
  type: string
- description: 'Dimensions of the 3DS2 challenge window to be displayed to the cardholder. Possible values: * **01** - size of 250x400 * **02** - size of 390x400 * **03** - size of 500x600 * **04** - size of 600x400 '
  name: challengeWindowSize
  type: string
- description: Indicates if you want to perform 3D Secure authentication on a transaction. > Alternatively, you can use [Dynamic 3D Secure](/risk-management/dynamic-3d-secure) to configure rules for applying 3D Secu
  name: executeThreeD
  type: string
- description: In case of Secure+, this field must be set to **CUPSecurePlus**.
  name: mpiImplementationType
  type: string
- description: Indicates the [exemption type](https://docs.adyen.com/payments-fundamentals/psd2-sca-compliance-and-implementation-guide#specifypreferenceinyourapirequest) that you want to request for the transaction
  name: scaExemption
  type: string
- description: Indicates your preference for the 3D Secure version. > If you use this parameter, you override the checks from Adyen's Authentication Engine. We recommend to use this field only if you have an extensi
  name: threeDSVersion
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-additional-data3-d-secure-schema.json
slug: payments-additional-data3-d-secure
tags:
- Payments
- Financial Services
- Fintech
title: AdditionalData3DSecure
---
