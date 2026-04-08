---
aid: sendgrid:sendgrid-createscheduledsend
name: Cancel or pause a scheduled send
tags:
- Scheduled Sends
humanURL: 
properties: []
description: >-
  **This endpoint allows you to cancel or pause a scheduled send associated with a `batch_id`.**  Passing this endpoint a `batch_id` and status will cancel or pause the scheduled send.  Once a scheduled send is set to `pause` or `cancel` you must use the "Update a scheduled send" endpoint to change its status or the "Delete a cancellation or pause from a scheduled send" endpoint to remove the status. Passing a status change to a scheduled send that has already been paused or cancelled will resu...

---
