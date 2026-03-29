---
aid: adyen:adyen-post-voidpendingrefund
name: Cancel an in-person refund
tags:
- - - - Modifications
humanURL: 
properties: []
description: >-
  This endpoint allows you to cancel an unreferenced refund request before it has been completed.  In your call, you can refer to the original refund request either by using the `tenderReference`, or the `pspReference`. We recommend implementing based on the `tenderReference`, as this is generated for both offline and online transactions.  For more information, refer to [Cancel an unreferenced refund](https://docs.adyen.com/point-of-sale/refund-payment/cancel-unreferenced).

---
