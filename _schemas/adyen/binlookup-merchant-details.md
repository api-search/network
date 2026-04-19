---
description: MerchantDetails schema from Adyen API
layout: schema
name: MerchantDetails
properties_list:
- description: 2-letter ISO 3166 country code of the card acceptor location. > This parameter is required for the merchants who don't use Adyen as the payment authorisation gateway.
  name: countryCode
  type: string
- description: If true, indicates that the merchant is enrolled in 3D Secure for the card network.
  name: enrolledIn3DSecure
  type: boolean
- description: The merchant category code (MCC) is a four-digit number which relates to a particular market segment. This code reflects the predominant activity that is conducted by the merchant. The list of MCCs ca
  name: mcc
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/binlookup-merchant-details-schema.json
slug: binlookup-merchant-details
tags:
- Payments
- Financial Services
- Fintech
title: MerchantDetails
---
