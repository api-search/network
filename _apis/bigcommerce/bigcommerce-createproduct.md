---
aid: bigcommerce:bigcommerce-createproduct
name: Create a Product
tags:
- Products
humanURL: 
properties: []
description: >-
  Creates a *Product*. Only one product can be created at a time; however, you can create multiple product variants using the `variants` array.  **Required Fields:** - `name` - `type` - `weight` - `price`  **Read-Only Fields** - `id` - `date_created` - `date_modified` - `calculated_price` - `base_variant_id`  **Limits** - 250 characters product name length. - A product can have up to 1000 images. Each image file or image uploaded by URL can be up to 8 MB.  **Usage Notes** * You can create multi...

---
