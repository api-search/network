---
aid: bigcommerce:bigcommerce-updatecheckoutconsignment
name: Update a Consignment
tags:
- Checkout Consignments
humanURL: 
properties: []
description: >-
  Updates an existing consignment. An update is either one of the following:  1. Updates the consignment address and/or line items. 2. Selects a specific fulfillment option.  ### Update the consignment address and line items For this type of update, the payload is the same as when creating a new consignment.         Update each *Consignment* `shippingOptionId` (shipping address and line items) with the `availableShippingOption > id` from the POST `/consignment` response.   **Note:** Updating a ...

---
