---
description: Enables a Merchant to supply their existing 3-D Secure (3DS) integration details at the time of Digital Payment Application (DPA) registration.
layout: schema
name: ThreeDSDefaultData
properties_list:
- description: Allows a Merchant to set a default Acquirer. An Acquirer BIN is an identifier assigned by Mastercard to an Acquirer. If this field is not defined and acquirerData has only one entry, this field will b
  name: defaultAcquirerBin
  type: string
- description: An identifier assigned to the Merchant by their Acquirer. If this field is not populated and acquirerData has only one entry, this field will be populated with the value from acquirerMerchantId.
  name: defaultAcquirerMerchantId
  type: string
- description: Allows a Merchant to set a default Merchant Country Code (CC). A Merchant CC is a two-character code indicating the country the Merchant is doing business in.
  name: defaultMerchantCountryCode
  type: string
- description: Allows a Merchant to set a default Merchant Category Code (MCC). An MCC is a four-character code assigned by Mastercard to the Merchant that indicates the type of business, service, or product provide
  name: defaultMerchantCategoryCode
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-unified-checkout-solutions-three-ds-default-data-schema.json
slug: mastercard-unified-checkout-solutions-three-ds-default-data
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: ThreeDSDefaultData
---
