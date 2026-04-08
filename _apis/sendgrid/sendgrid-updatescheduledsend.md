---
aid: sendgrid:sendgrid-updatescheduledsend
name: Update a scheduled send
tags:
- Scheduled Sends
humanURL: 
properties: []
description: >-
  **This endpoint allows you to update the status of a scheduled send for the given `batch_id`.**  If you have already set a `cancel` or `pause` status on a scheduled send using the "Cancel or pause a scheduled send" endpoint, you can update it's status using this endpoint. Attempting to update a status once it has been set with the "Cancel or pause a scheduled send" endpoint will result in a `400` error.

---
