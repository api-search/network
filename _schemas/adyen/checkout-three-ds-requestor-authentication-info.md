---
description: ThreeDSRequestorAuthenticationInfo schema from Adyen API
layout: schema
name: ThreeDSRequestorAuthenticationInfo
properties_list:
- description: 'Data that documents and supports a specific authentication process. Maximum length: 2048 bytes.'
  name: threeDSReqAuthData
  type: string
- description: 'Mechanism used by the Cardholder to authenticate to the 3DS Requestor. Allowed values: * **01** — No 3DS Requestor authentication occurred (for example, cardholder “logged in” as guest). * **02** — Lo'
  name: threeDSReqAuthMethod
  type: string
- description: 'Date and time in UTC of the cardholder authentication. Format: YYYYMMDDHHMM'
  name: threeDSReqAuthTimestamp
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-three-ds-requestor-authentication-info-schema.json
slug: checkout-three-ds-requestor-authentication-info
tags:
- Payments
- Financial Services
- Fintech
title: ThreeDSRequestorAuthenticationInfo
---
