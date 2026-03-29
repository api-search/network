---
aid: bigcommerce:bigcommerce-createcheckoutconsignment
name: Create a Consignment
tags:
- Checkout Consignments
humanURL: 
properties: []
description: >-
  Adds a new *Consignment* to *Checkout*.  Perform the following two steps to define the fulfillment of the items in the cart.   ### For **shipping** consignments:     1. Add a new Consignment to Checkout.         * Send a `POST` request to `/consignments` with each shipping address, line item IDs, and quantities. Each address can have its own line item IDs.         * Provide a full valid customer address before placing the order. If provided, the order placement will succeed.          * As par...

---
