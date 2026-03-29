---
aid: bigcommerce:bigcommerce-deletepages
name: Delete Pages
tags:
- Pages (Bulk)
humanURL: 
properties: []
description: >-
  Deletes one or more content pages. This endpoint supports bulk operations.  > #### Warning > **Pay attention to query parameters** > If you attempt to delete multiple pages by passing more than one page ID to `id:in` and one or more of them does not exist, you will receive a 404 response. However, the pages corresponding to the page IDs that do exist will still be deleted.

---
