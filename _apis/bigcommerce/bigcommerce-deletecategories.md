---
aid: bigcommerce:bigcommerce-deletecategories
name: Delete Categories
tags:
- Categories (deprecated)
humanURL: 
properties: []
description: >-
  When possible, use the [Category Trees - Delete categories](/docs/rest-catalog/category-trees/categories#delete-categories) endpoint instead.  Deletes *Category* objects. At least one filter parameter is required to perform the `DELETE` operation.  **Usage Notes**  - Sending a `DELETE`request without specifying a filter parameter will result in a `422` error.  - Sending a `DELETE` request for a category that contains products will result in a `422` error. Move products to a new category by se...

---
