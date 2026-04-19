---
description: ThreeDS2Result schema from Adyen API
layout: schema
name: ThreeDS2Result
properties_list:
- description: The `authenticationValue` value as defined in the 3D Secure 2 specification.
  name: authenticationValue
  type: string
- description: The algorithm used by the ACS to calculate the authentication value, only for Cartes Bancaires integrations.
  name: cavvAlgorithm
  type: string
- description: Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has been cancelled. For possible values, refer to [3D Secure API reference](https://docs.adyen
  name: challengeCancel
  type: string
- description: The `dsTransID` value as defined in the 3D Secure 2 specification.
  name: dsTransID
  type: string
- description: The `eci` value as defined in the 3D Secure 2 specification.
  name: eci
  type: string
- description: 'Indicates the exemption type that was applied by the issuer to the authentication, if exemption applied. Allowed values: * `lowValue` * `secureCorporate` * `trustedBeneficiary` * `transactionRiskAnaly'
  name: exemptionIndicator
  type: string
- description: The `messageVersion` value as defined in the 3D Secure 2 specification.
  name: messageVersion
  type: string
- description: Risk score calculated by Cartes Bancaires Directory Server (DS).
  name: riskScore
  type: string
- description: 'Indicates whether a challenge is requested for this transaction. Possible values: * **01** — No preference * **02** — No challenge requested * **03** — Challenge requested (3DS Requestor preference) *'
  name: threeDSRequestorChallengeInd
  type: string
- description: The `threeDSServerTransID` value as defined in the 3D Secure 2 specification.
  name: threeDSServerTransID
  type: string
- description: The `timestamp` value of the 3D Secure 2 authentication.
  name: timestamp
  type: string
- description: The `transStatus` value as defined in the 3D Secure 2 specification.
  name: transStatus
  type: string
- description: Provides information on why the `transStatus` field has the specified value. For possible values, refer to [our docs](https://docs.adyen.com/online-payments/3d-secure/api-reference#possible-transstatu
  name: transStatusReason
  type: string
- description: The `whiteListStatus` value as defined in the 3D Secure 2 specification.
  name: whiteListStatus
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-three-ds2-result-schema.json
slug: payments-three-ds2-result
tags:
- Payments
- Financial Services
- Fintech
title: ThreeDS2Result
---
