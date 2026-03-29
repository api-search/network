---
aid: bigcommerce:bigcommerce-getcustomsinformation
name: Get Customs Information
tags:
- Customs Information
humanURL: 
properties: []
description: >-
  Get customs information for products.  This list can be filtered to return customs information objects specific to a list of requested product_ids. This is achieved by appending the query string `?product_id:in=4,5,6` to the resource `/shipping/products/customs-information`.  ```http GET /shipping/products/customs-information?product_id:in=4,5,6 ```

---
