---
aid: bigcommerce:bigcommerce-updatecustomerssettingschannel
name: Update Customer Settings per Channel
tags:
- Channel Settings
humanURL: 
properties: []
description: >-
  Update the customer settings per channel  **Required Fields**  * `channel_id`: Provide a `channel_id` array containing one or more channel IDs. Customers will have access to these channels and no others. This array cannot be empty.  **Notes**  * Setting `null` will delete override per given channel, and values will be inherited from the global level. Make sure the channel has `allow_global_logins` enabled.

---
