---
aid: zendesk:zendesk-createorupdateuserfieldoption
name: Zendesk Post  Api V2 User_fields User_field_id Options
tags:
- User Fields
humanURL: 
properties: []
description: >-
  Creates a new option or updates an existing option for the given drop-down user field.  To update an option, include the id of the option in the `custom_field_option` object. Example: `{"custom_field_option": {"id": 10002, "name": "Pineapples", ... }`. If an option exists for the given ID, the option will be updated. Otherwise, a new option will be created.  #### Response  Returns one of the following status codes:  - 200 with `Location: /api/v2/user_fields/{user_field_id}/options.json` if th...

---
