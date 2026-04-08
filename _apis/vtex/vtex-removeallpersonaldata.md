---
aid: vtex:vtex-removeallpersonaldata
name: VTex Remove all personal data from shopping cart
tags:
- Shopping Cart
humanURL: 
properties: []
description: >-
  This call removes all user information, making a cart anonymous while leaving the items.  The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure that represents a shopping cart and contains all information about it. Hence, the `orderFormId` is the identification code of a given cart.  This call works by creating a new orderForm, setting a new cookie, and returning a redirect 302 to the cart URL (`/checkout/#/orderform`).  ## Permissions  Any us...

---
