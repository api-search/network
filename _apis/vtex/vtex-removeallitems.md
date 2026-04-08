---
aid: vtex:vtex-removeallitems
name: VTex Remove all items from shopping cart
tags:
- Shopping Cart
humanURL: 
properties: []
description: >-
  This request removes all items from a given cart, leaving it empty.  You must send an empty JSON in the body of the request.  The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the `orderFormId` is the identification code of a given cart.  >ℹ️ Request body must always be sent with empty value "{ }" in this endpoint.  ## Permissions  Any user or [applica...

---
