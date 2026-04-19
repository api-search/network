---
description: ThreeDSRequestData schema from Adyen API
layout: schema
name: ThreeDSRequestData
properties_list:
- description: 'Dimensions of the 3DS2 challenge window to be displayed to the cardholder. Possible values: * **01** - size of 250x400 * **02** - size of 390x400 * **03** - size of 500x600 * **04** - size of 600x400 '
  name: challengeWindowSize
  type: string
- description: Flag for data only flow.
  name: dataOnly
  type: string
- description: 'Indicates if [native 3D Secure authentication](https://docs.adyen.com/online-payments/3d-secure/native-3ds2) should be used when available. Possible values: * **preferred**: Use native 3D Secure authe'
  name: nativeThreeDS
  type: string
- description: 'The version of 3D Secure to use. Possible values: * **2.1.0** * **2.2.0**'
  name: threeDSVersion
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-three-ds-request-data-schema.json
slug: checkout-three-ds-request-data
tags:
- Payments
- Financial Services
- Fintech
title: ThreeDSRequestData
---
