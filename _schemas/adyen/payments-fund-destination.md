---
description: FundDestination schema from Adyen API
layout: schema
name: FundDestination
properties_list:
- description: a map of name/value pairs for passing in additional/industry-specific data
  name: additionalData
  type: object
- description: The address where to send the invoice.
  name: billingAddress
  type: object
- description: Credit card data. Optional if `shopperReference` and `selectedRecurringDetailReference` are provided.
  name: card
  type: object
- description: The `recurringDetailReference` you want to use for this payment. The value `LATEST` can be used to select the most recently stored recurring detail.
  name: selectedRecurringDetailReference
  type: string
- description: the email address of the person
  name: shopperEmail
  type: string
- description: the name of the person
  name: shopperName
  type: object
- description: 'Required for recurring payments. Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters. > Your reference must not include personally identif'
  name: shopperReference
  type: string
- description: Required for Back-to-Back/ purchase driven load in Wallet transactions. Contains the final merchant who will be receiving the money, also known as subMerchant, information.
  name: subMerchant
  type: object
- description: the telephone number of the person
  name: telephoneNumber
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-fund-destination-schema.json
slug: payments-fund-destination
tags:
- Payments
- Financial Services
- Fintech
title: FundDestination
---
