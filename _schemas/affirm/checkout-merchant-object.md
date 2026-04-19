---
description: Merchant-specific configuration for the checkout, including callback URLs and the public API key.
layout: schema
name: MerchantObject
properties_list:
- description: The merchant's public API key. Required for checkout and store endpoints when submitting from a server context.
  name: public_api_key
  type: string
- description: The URL the customer is redirected to after successfully completing the Affirm checkout flow. A checkout_token is delivered to this URL via POST or GET depending on user_confirmation_url_action.
  name: user_confirmation_url
  type: string
- description: The URL the customer is redirected to if they cancel or abandon the Affirm checkout flow.
  name: user_cancel_url
  type: string
- description: Determines how the checkout_token is delivered to the user_confirmation_url. "POST" sends it as a form body field; "GET" appends it as a query parameter.
  name: user_confirmation_url_action
  type: string
- description: The merchant's display name, shown to customers during checkout.
  name: name
  type: string
provider_name: affirm
provider_slug: affirm
schema_file: json-schema/checkout-merchant-object-schema.json
slug: checkout-merchant-object
tags: []
title: MerchantObject
---
