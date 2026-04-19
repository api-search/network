---
description: PublicKeyResponse schema from Adyen API
layout: schema
name: PublicKeyResponse
properties_list:
- description: The public key to be used for encrypting the symmetric session key.
  name: publicKey
  type: string
- description: The expiry date of the public key.
  name: publicKeyExpiryDate
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-public-key-response-schema.json
slug: configuration-public-key-response
tags:
- Payments
- Financial Services
- Fintech
title: PublicKeyResponse
---
