---
description: AuthenticationInfo schema from Adyen API
layout: schema
name: AuthenticationInfo
properties_list:
- description: Universally unique transaction identifier assigned by the Access Control Server (ACS) to identify a single transaction.
  name: acsTransId
  type: string
- description: Information about Strong Customer Authentication (SCA). Returned when `type` is **challenge**.
  name: challenge
  type: object
- description: 'Specifies a preference for receiving a challenge. Possible values: * **01**: No preference * **02**: No challenge requested * **03**: Challenge requested (preference) * **04**: Challenge requested (ma'
  name: challengeIndicator
  type: string
- description: 'Date and time in UTC of the cardholder authentication. [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format: YYYY-MM-DDThh:mm:ss+TZD, for example, **2020-12-18T10:15:30+01:00**.'
  name: createdAt
  type: string
- description: 'Indicates the type of channel interface being used to initiate the transaction. Possible values: * **app** * **browser** * **3DSRequestorInitiated** (initiated by a merchant when the cardholder is not'
  name: deviceChannel
  type: string
- description: Universally unique transaction identifier assigned by the DS (card scheme) to identify a single transaction.
  name: dsTransID
  type: string
- description: 'Indicates the exemption type that was applied to the authentication by the issuer, if exemption applied. Possible values: * **lowValue** * **secureCorporate** * **trustedBeneficiary** * **transactionR'
  name: exemptionIndicator
  type: string
- description: Indicates if the purchase was in the PSD2 scope.
  name: inPSD2Scope
  type: boolean
- description: 'Identifies the category of the message for a specific use case. Possible values: * **payment** * **nonPayment**'
  name: messageCategory
  type: string
- description: The `messageVersion` value as defined in the 3D Secure 2 specification.
  name: messageVersion
  type: string
- description: Risk score calculated from the transaction rules.
  name: riskScore
  type: integer
- description: The `threeDSServerTransID` value as defined in the 3D Secure 2 specification.
  name: threeDSServerTransID
  type: string
- description: 'The `transStatus` value as defined in the 3D Secure 2 specification. Possible values: * **Y**: Authentication / Account verification successful. * **N**: Not Authenticated / Account not verified. Tran'
  name: transStatus
  type: string
- description: Provides information on why the `transStatus` field has the specified value. For possible values, refer to [our docs](https://docs.adyen.com/online-payments/3d-secure/api-reference#possible-transstatu
  name: transStatusReason
  type: string
- description: 'The type of authentication performed. Possible values: * **frictionless** * **challenge**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/authentication-webhooks-authentication-info-schema.json
slug: authentication-webhooks-authentication-info
tags:
- Payments
- Financial Services
- Fintech
title: AuthenticationInfo
---
