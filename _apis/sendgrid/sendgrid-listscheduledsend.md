---
aid: sendgrid:sendgrid-listscheduledsend
name: Retrieve all scheduled sends
tags:
- Scheduled Sends
humanURL: 
properties: []
description: >-
  **This endpoint allows you to retrieve all cancelled and paused scheduled send information.**  This endpoint will return only the scheduled sends that are associated with a `batch_id`. If you have scheduled a send using the `/mail/send` endpoint and the `send_at` field but no `batch_id`, the send will be scheduled for delivery; however, it will not be returned by this endpoint. For this reason, you should assign a `batch_id` to any scheduled send you may need to pause or cancel in the future.

---
