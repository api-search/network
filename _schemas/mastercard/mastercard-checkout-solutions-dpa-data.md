---
description: DpaData Object for Integrator to populate Digital Payment Application (DPA) information, including the Merchant name, address, and other relevant data.
layout: schema
name: DpaData
properties_list:
- description: 'The name of the Merchant that the Cardholder will see when checking out with the Digital Payment Application (DPA). Conditional: Required for Guest Checkout Tokenization (GCT) and SQR programs.'
  name: dpaPresentationName
  type: string
- description: Legal name of Merchant (which may differ from dpaPresentationName).
  name: dpaName
  type: string
- description: URI for the logo displayed to Cardholders during C2P checkout.
  name: dpaLogoUri
  type: string
- description: Digital Payment Application (DPA) identifier. This field may contain the DPA website URI, a mobile application identifier, or another unique identifier (UUID, URL, APK package name, etc.).
  name: dpaUri
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-checkout-solutions-dpa-data-schema.json
slug: mastercard-checkout-solutions-dpa-data
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: DpaData
---
