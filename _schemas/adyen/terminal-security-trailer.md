---
description: It contains information related to the security of the message. SecurityTrailer as used by Adyen.
layout: schema
name: SecurityTrailer
properties_list:
- description: ''
  name: AdyenCryptoVersion
  type: integer
- description: ''
  name: KeyIdentifier
  type: string
- description: ''
  name: KeyVersion
  type: integer
- description: ''
  name: Nonce
  type: string
- description: ''
  name: Hmac
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-security-trailer-schema.json
slug: terminal-security-trailer
tags:
- Payments
- Financial Services
- Fintech
title: SecurityTrailer
---
