---
aid: adyen:adyen-patch-companies-companyid-terminalorders-orderid
name: Update an order
tags:
- - - - Terminal orders - company level
humanURL: 
properties: []
description: >-
  Updates the terminal products order identified in the path. Updating is only possible while the order has the status **Placed**.  The request body only needs to contain what you want to change.  However, to update the products in the `items` array, you must provide the entire array. For example, if the array has three items:  To remove one item, the array must include the remaining two items. Or to add one item, the array must include all four items.  To make this request, your API credential...

---
