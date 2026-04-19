---
description: PayoutMethod schema from Adyen API
layout: schema
name: PayoutMethod
properties_list:
- description: The [`merchantAccount`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__reqParam_merchantAccount) you used in the `/payments` request when you [saved the account holder's c
  name: merchantAccount
  type: string
- description: Adyen-generated unique alphanumeric identifier (UUID) for the payout method, returned in the response when you create a payout method. Required when updating an existing payout method in an `/updateAc
  name: payoutMethodCode
  type: string
- description: Your reference for the payout method.
  name: payoutMethodReference
  type: string
- description: The [`recurringDetailReference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_additionalData-ResponseAdditionalDataCommon-recurring-recurringDetailReference) re
  name: recurringDetailReference
  type: string
- description: The [`shopperReference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__reqParam_shopperReference) you sent in the `/payments` request when you [saved the account holder's
  name: shopperReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-payout-method-schema.json
slug: notifications-payout-method
tags:
- Payments
- Financial Services
- Fintech
title: PayoutMethod
---
