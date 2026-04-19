---
description: ThreeDSecureData schema from Adyen API
layout: schema
name: ThreeDSecureData
properties_list:
- description: In 3D Secure 1, the authentication response if the shopper was redirected. In 3D Secure 2, this is the `transStatus` from the challenge result. If the transaction was frictionless, omit this parameter
  name: authenticationResponse
  type: string
- description: The cardholder authentication value (base64 encoded, 20 bytes in a decoded form).
  name: cavv
  type: string
- description: The CAVV algorithm used. Include this only for 3D Secure 1.
  name: cavvAlgorithm
  type: string
- description: Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has been cancelled. For possible values, refer to [3D Secure API reference](https://docs.adyen
  name: challengeCancel
  type: string
- description: In 3D Secure 1, this is the enrollment response from the 3D directory server. In 3D Secure 2, this is the `transStatus` from the `ARes`.
  name: directoryResponse
  type: string
- description: Supported for 3D Secure 2. The unique transaction identifier assigned by the Directory Server (DS) to identify a single transaction.
  name: dsTransID
  type: string
- description: The electronic commerce indicator.
  name: eci
  type: string
- description: Risk score calculated by Directory Server (DS). Required for Cartes Bancaires integrations.
  name: riskScore
  type: string
- description: The version of the 3D Secure protocol.
  name: threeDSVersion
  type: string
- description: Network token authentication verification value (TAVV). The network token cryptogram.
  name: tokenAuthenticationVerificationValue
  type: string
- description: Provides information on why the `transStatus` field has the specified value. For possible values, refer to [our docs](https://docs.adyen.com/online-payments/3d-secure/api-reference#possible-transstatu
  name: transStatusReason
  type: string
- description: Supported for 3D Secure 1. The transaction identifier (Base64-encoded, 20 bytes in a decoded form).
  name: xid
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-three-d-secure-data-schema.json
slug: checkout-three-d-secure-data
tags:
- Payments
- Financial Services
- Fintech
title: ThreeDSecureData
---
