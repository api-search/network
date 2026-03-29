---
aid: adyen:adyen-post-companies-companyid-terminalorders-orderid-cancel
name: Cancel an order
tags:
- - - - Terminal orders - company level
humanURL: 
properties: []
description: >-
  Cancels the terminal products order identified in the path. Cancelling is only possible while the order has the status **Placed**. To cancel an order, make a POST call without a request body. The response returns the full order details, but with the status changed to **Cancelled**.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read and write

---
