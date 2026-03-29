---
aid: bigcommerce:bigcommerce-createcoupon
name: Create a New Coupon
tags:
- Coupons
humanURL: 
properties: []
description: >-
  Creates a *Coupon*.  **Required Fields** *   `name` *   `code` *   `type` *   `amount` *   `applies_to`  **Read Only Fields** *   `id` *   `num_uses`  **Notes**  The coupon type can be one of the following:  *   `per_item_discount` *   `per_total_discount` *   `shipping_discount` *   `free_shipping` *   `percentage_discount`  Legacy coupon codes only work with the store's default currency. Applying a coupon with any other currency other than the store's default will result in the error: "Coup...

---
