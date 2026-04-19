---
description: ChallengeInfo schema from Adyen API
layout: schema
name: ChallengeInfo
properties_list:
- description: Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has been cancelled. For possible values, refer to [3D Secure API reference](https://docs.adyen
  name: challengeCancel
  type: string
- description: 'The flow used in the challenge. Possible values: * **OTP_SMS**: one-time password (OTP) flow * **OOB**: out-of-band (OOB) flow'
  name: flow
  type: string
- description: The last time of interaction with the challenge.
  name: lastInteraction
  type: string
- description: The last four digits of the phone number used in the challenge.
  name: phoneNumber
  type: string
- description: The number of times the one-time password (OTP) was resent during the challenge.
  name: resends
  type: integer
- description: The number of retries used in the challenge.
  name: retries
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/authentication-webhooks-challenge-info-schema.json
slug: authentication-webhooks-challenge-info
tags:
- Payments
- Financial Services
- Fintech
title: ChallengeInfo
---
