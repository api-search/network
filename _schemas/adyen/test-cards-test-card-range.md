---
description: TestCardRange schema from Adyen API
layout: schema
name: TestCardRange
properties_list:
- description: Contains the billing address of the card holder. The address details need to be AVS-compliant, which means that you need to provide at least street address.
  name: address
  type: object
- description: The name of the card holder, as it appears on the card, for the test card range.
  name: cardHolderName
  type: string
- description: 'The test card range security code. Example: 123'
  name: cvc
  type: string
- description: 'Expiry month for the test card range. Allowed values: * JANUARY * FEBRUARY * MARCH * APRIL * MAY * JUNE * JULY * AUGUST * SEPTEMBER * OCTOBER * NOVEMBER * DECEMBER'
  name: expiryMonth
  type: string
- description: 'Expiry year for the test card range. Example: 2020'
  name: expiryYear
  type: integer
- description: 'The last test card number in the test card range (inclusive): * Min 6, max 19 digits * BIN compliant Example: 5432 1234 1234 4321'
  name: rangeEnd
  type: string
- description: 'The first test card number in the test card range (inclusive): * Min 6, max 19 digits * BIN compliant Example: 5432 1234 1234 1234'
  name: rangeStart
  type: string
- description: '3D Secure server response. It notifies whether the specified card holder is enrolled in a 3D Secure service. Possible values: * Y (Authentication available) * N (Card holder not enrolled/not participa'
  name: threeDDirectoryServerResponse
  type: string
- description: The password used for 3D Secure authentication.
  name: threeDPassword
  type: string
- description: The username used for 3D Secure authentication.
  name: threeDUsername
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/test-cards-test-card-range-schema.json
slug: test-cards-test-card-range
tags:
- Payments
- Financial Services
- Fintech
title: TestCardRange
---
