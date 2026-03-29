---
aid: bigcommerce:bigcommerce-updatesettingsinventorynotifications
name: Update Inventory Notifications Settings
tags:
- Inventory Notifications
humanURL: 
properties: []
description: >-
  Updates inventory notification settings.  * `channel_id` can be used as a query parameter to get inventory notification settings per channel. If omitted, you will interact with the global setting only.  * Supplying `null` settings values per channel will delete overrides per given channel and values will be inherited from global level.  * Partial updates are not supported within the given endpoint. In order to delete overrides per channel, `null` should be supplied for all the settings within...

---
