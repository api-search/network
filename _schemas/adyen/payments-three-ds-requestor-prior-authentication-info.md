---
description: ThreeDSRequestorPriorAuthenticationInfo schema from Adyen API
layout: schema
name: ThreeDSRequestorPriorAuthenticationInfo
properties_list:
- description: 'Data that documents and supports a specific authentication process. Maximum length: 2048 bytes.'
  name: threeDSReqPriorAuthData
  type: string
- description: 'Mechanism used by the Cardholder to previously authenticate to the 3DS Requestor. Allowed values: * **01** — Frictionless authentication occurred by ACS. * **02** — Cardholder challenge occurred by AC'
  name: threeDSReqPriorAuthMethod
  type: string
- description: 'Date and time in UTC of the prior cardholder authentication. Format: YYYYMMDDHHMM'
  name: threeDSReqPriorAuthTimestamp
  type: string
- description: This data element provides additional information to the ACS to determine the best approach for handing a request. This data element contains an ACS Transaction ID for a prior authenticated transactio
  name: threeDSReqPriorRef
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-three-ds-requestor-prior-authentication-info-schema.json
slug: payments-three-ds-requestor-prior-authentication-info
tags:
- Payments
- Financial Services
- Fintech
title: ThreeDSRequestorPriorAuthenticationInfo
---
