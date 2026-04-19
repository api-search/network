---
description: EcontextVoucherDetails schema from Adyen API
layout: schema
name: EcontextVoucherDetails
properties_list:
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The shopper's first name.
  name: firstName
  type: string
- description: The shopper's last name.
  name: lastName
  type: string
- description: The shopper's email.
  name: shopperEmail
  type: string
- description: The shopper's contact number. It must have an international number format, for example **+31 20 779 1846**. Formats like **+31 (0)20 779 1846** or **0031 20 779 1846** are not accepted.
  name: telephoneNumber
  type: string
- description: '**econtextvoucher**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-econtext-voucher-details-schema.json
slug: checkout-econtext-voucher-details
tags:
- Payments
- Financial Services
- Fintech
title: EcontextVoucherDetails
---
