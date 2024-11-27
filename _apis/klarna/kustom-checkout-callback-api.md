---
aid: klarna:kustom-checkout-callback-api
name: Checkout API V3
tags:
  - Checkout
humanURL: https://docs.klarna.com/api/checkout-merchant/
properties:
  - url: https://docs.klarna.com/api/checkout-merchant/
    name: Kustom Checkout Callback API
    type: Documentation
    description: >-
      Klarna provides a number of different callbacks during the customer's
      checkout session. The callbacks can be used to update the order when the
      customer changes their address as well as to do a final check to validate
      the order before it is submitted.
  - url: properties/kustom-checkout-callback-api-openapi.yml
    type: OpenAPI
description: >-
  Klarna provides a number of different callbacks during the customer's checkout
  session. The callbacks can be used to update the order when the customer
  changes their address as well as to do a final check to validate the order
  before it is submitted. The callbacks are sent as POST requests to the
  endpoint you specify when creating the order. Your response is interpreted
  using the response code and body. Read more on
  [here](https://docs.klarna.com/kco/).

---