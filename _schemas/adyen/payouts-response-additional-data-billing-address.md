---
description: ResponseAdditionalDataBillingAddress schema from Adyen API
layout: schema
name: ResponseAdditionalDataBillingAddress
properties_list:
- description: The billing address city passed in the payment request.
  name: billingAddress.city
  type: string
- description: 'The billing address country passed in the payment request. Example: NL'
  name: billingAddress.country
  type: string
- description: The billing address house number or name passed in the payment request.
  name: billingAddress.houseNumberOrName
  type: string
- description: 'The billing address postal code passed in the payment request. Example: 1011 DJ'
  name: billingAddress.postalCode
  type: string
- description: 'The billing address state or province passed in the payment request. Example: NH'
  name: billingAddress.stateOrProvince
  type: string
- description: The billing address street passed in the payment request.
  name: billingAddress.street
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payouts-response-additional-data-billing-address-schema.json
slug: payouts-response-additional-data-billing-address
tags:
- Payments
- Financial Services
- Fintech
title: ResponseAdditionalDataBillingAddress
---
