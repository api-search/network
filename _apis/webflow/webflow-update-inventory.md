---
aid: webflow:webflow-update-inventory
name: Webflow Update Item Inventory
tags:
- Inventory
humanURL: 
properties: []
description: >-
  Updates the current inventory levels for a particular SKU item.  Updates may be given in one or two methods, absolutely or incrementally. - Absolute updates are done by setting `quantity` directly. - Incremental updates are by specifying the inventory delta in `updateQuantity` which is then added to the `quantity` stored on the server.  Required scope | `ecommerce:write`

---
