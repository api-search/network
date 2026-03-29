---
aid: bigcommerce:bigcommerce-addcartlineitems
name: Add Cart Line Items
tags:
- Items
humanURL: 
properties: []
description: >-
  Adds line item to the *Cart*.  **Usage Notes**  To add a custom item use `custom_items`.   Overriding a product’s `list_price` will make that item ineligible for V3 product level promotions.  If a product has modifiers, omit the `variant_id` and instead use the `option_selections` array to describe both the **variant** and the **modifier** selections.  Please note that this API endpoint is not concurrent safe, meaning multiple simultaneous requests could result in unexpected and inconsistent ...

---
