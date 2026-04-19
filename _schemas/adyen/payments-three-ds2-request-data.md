---
description: ThreeDS2RequestData schema from Adyen API
layout: schema
name: ThreeDS2RequestData
properties_list:
- description: Additional information about the Cardholder’s account provided by the 3DS Requestor.
  name: acctInfo
  type: object
- description: 'Indicates the type of account. For example, for a multi-account card product. Length: 2 characters. Allowed values: * **01** — Not applicable * **02** — Credit * **03** — Debit'
  name: acctType
  type: string
- description: Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The acquiring BIN enrolled for 3D Secure 2. This string should mat
  name: acquirerBIN
  type: string
- description: 'Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The merchantId that is enrolled for 3D Secure 2 by the merchant''s '
  name: acquirerMerchantID
  type: string
- description: 'Indicates whether the Cardholder Shipping Address and Cardholder Billing Address are the same. Allowed values: * **Y** — Shipping Address matches Billing Address. * **N** — Shipping Address does not m'
  name: addrMatch
  type: string
- description: If set to true, you will only perform the [3D Secure 2 authentication](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only), and not the payment authorisation.
  name: authenticationOnly
  type: boolean
- description: 'Possibility to specify a preference for receiving a challenge from the issuer. Allowed values: * `noPreference` * `requestNoChallenge` * `requestChallenge` * `requestChallengeAsMandate`'
  name: challengeIndicator
  type: string
- description: 'The environment of the shopper. Allowed values: * `app` * `browser`'
  name: deviceChannel
  type: string
- description: Display options for the 3D Secure 2 SDK. Optional and only for `deviceChannel` **app**.
  name: deviceRenderOptions
  type: object
- description: The home phone number provided by the Cardholder.
  name: homePhone
  type: object
- description: Required for merchants that have been enrolled for 3D Secure 2 by another party than Adyen, mostly [authentication-only integrations](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/a
  name: mcc
  type: string
- description: 'Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The merchant name that the issuer presents to the shopper if they '
  name: merchantName
  type: string
- description: The `messageVersion` value indicating the 3D Secure 2 protocol version.
  name: messageVersion
  type: string
- description: The mobile phone number provided by the Cardholder.
  name: mobilePhone
  type: object
- description: URL to where the issuer should send the `CRes`. Required if you are not using components for `channel` **Web** or if you are using classic integration `deviceChannel` **browser**.
  name: notificationURL
  type: string
- description: Value **true** indicates that the transaction was de-tokenised prior to being received by the ACS.
  name: payTokenInd
  type: boolean
- description: Indicates the type of payment for which an authentication is requested (message extension)
  name: paymentAuthenticationUseCase
  type: string
- description: 'Indicates the maximum number of authorisations permitted for instalment payments. Length: 1–3 characters.'
  name: purchaseInstalData
  type: string
- description: 'Date after which no further authorisations shall be performed. Format: YYYYMMDD'
  name: recurringExpiry
  type: string
- description: 'Indicates the minimum number of days between authorisations. Maximum length: 4 characters.'
  name: recurringFrequency
  type: string
- description: The `sdkAppID` value as received from the 3D Secure 2 SDK. Required for `deviceChannel` set to **app**.
  name: sdkAppID
  type: string
- description: The `sdkEncData` value as received from the 3D Secure 2 SDK. Required for `deviceChannel` set to **app**.
  name: sdkEncData
  type: string
- description: The `sdkEphemPubKey` value as received from the 3D Secure 2 SDK. Required for `deviceChannel` set to **app**.
  name: sdkEphemPubKey
  type: object
- description: The maximum amount of time in minutes for the 3D Secure 2 authentication process. Optional and only for `deviceChannel` set to **app**. Defaults to **60** minutes.
  name: sdkMaxTimeout
  type: integer
- description: The `sdkReferenceNumber` value as received from the 3D Secure 2 SDK. Only for `deviceChannel` set to **app**.
  name: sdkReferenceNumber
  type: string
- description: The `sdkTransID` value as received from the 3D Secure 2 SDK. Only for `deviceChannel` set to **app**.
  name: sdkTransID
  type: string
- description: Version of the 3D Secure 2 mobile SDK. Only for `deviceChannel` set to **app**.
  name: sdkVersion
  type: string
- description: Completion indicator for the device fingerprinting.
  name: threeDSCompInd
  type: string
- description: Indicates the type of Authentication request.
  name: threeDSRequestorAuthenticationInd
  type: string
- description: Information about how the 3DS Requestor authenticated the cardholder before or during the transaction
  name: threeDSRequestorAuthenticationInfo
  type: object
- description: 'Indicates whether a challenge is requested for this transaction. Possible values: * **01** — No preference * **02** — No challenge requested * **03** — Challenge requested (3DS Requestor preference) *'
  name: threeDSRequestorChallengeInd
  type: string
- description: Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only) for Visa. Unique 3D Secure requestor identifier assigned by the Dir
  name: threeDSRequestorID
  type: string
- description: Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only) for Visa. Unique 3D Secure requestor name assigned by the Directory
  name: threeDSRequestorName
  type: string
- description: Information about how the 3DS Requestor authenticated the cardholder as part of a previous 3DS transaction.
  name: threeDSRequestorPriorAuthenticationInfo
  type: object
- description: URL of the (customer service) website that will be shown to the shopper in case of technical errors during the 3D Secure 2 process.
  name: threeDSRequestorURL
  type: string
- description: 'Identifies the type of transaction being authenticated. Length: 2 characters. Allowed values: * **01** — Goods/Service Purchase * **03** — Check Acceptance * **10** — Account Funding * **11** — Quasi-'
  name: transType
  type: string
- description: Identify the type of the transaction being authenticated.
  name: transactionType
  type: string
- description: The `whiteListStatus` value returned from a previous 3D Secure 2 transaction, only applicable for 3D Secure 2 protocol version 2.2.0.
  name: whiteListStatus
  type: string
- description: The work phone number provided by the Cardholder.
  name: workPhone
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-three-ds2-request-data-schema.json
slug: payments-three-ds2-request-data
tags:
- Payments
- Financial Services
- Fintech
title: ThreeDS2RequestData
---
