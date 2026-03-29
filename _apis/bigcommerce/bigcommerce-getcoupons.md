---
aid: bigcommerce:bigcommerce-getcoupons
name: Get All Coupons
tags:
- Coupons
humanURL: 
properties: []
description: >-
  Returns a list of *Coupons*. Default sorting is by coupon/discount id, from lowest to highest. You can pass in optional filter parameters. We recommended using `?min_id=x&limit=y` to paginate through a large set of data because it offers better performance.  ## Usage Notes  Available types for `type` and `exclude_type` filters:  |Type| |-| |`per_item_discount`| |`percentage_discount`| |`per_total_discount`| |`shipping_discount`| |`free_shipping`| |`promotion`|  Coupons with `type=promotion` w...

---
