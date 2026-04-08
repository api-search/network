---
aid: zendesk:zendesk-createorupdateticketfieldoption
name: Zendesk Post  Api V2 Ticket_fields Ticket_field_id Options
tags:
- Ticket Fields
humanURL: 
properties: []
description: >-
  Creates or updates an option for the given drop-down ticket field.  To update an option, include the id of the option in the `custom_field_option` object. Example:  `{"custom_field_option": {"id": 10002, "name": "Pineapples", ... }`  If an option exists for the given ID, the option will be updated. Otherwise, a new option will be created.  #### Response  Returns one of the following status codes:  - 200 with `Location: /api/v2/ticket_fields/{ticket_field_id}/options.json` if the ticket field ...

---
