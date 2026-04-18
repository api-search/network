---
description: ''
layout: schema
name: DpaData
properties_list:
- description: Legal name of Merchant (which may differ from dpaPresentationName).
  name: dpaName
  type: string
- description: The name of the Merchant that the Cardholder will see when checking out with the Digital Payment Application (DPA).
  name: dpaPresentationName
  type: string
- description: Digital Payment Application (DPA) identifier. This field may contain the DPA website URI, a mobile application identifier, or another unique identifier (UUID, URL, APK package name, etc.).
  name: dpaUri
  type: string
- description: Website or URL where the payment experience is placed on the checkout page.
  name: originDomains
  type: array
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-unified-checkout-solutions-dpa-data-schema.json
slug: mastercard-unified-checkout-solutions-dpa-data
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: DpaData
---
