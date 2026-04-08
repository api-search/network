---
aid: sendgrid:sendgrid-deleteeventwebhook
name: Delete a single Event Webhook by ID.
tags:
- Event Webhook
humanURL: 
properties: []
description: >-
  **This endpoint allows you to delete a single Event Webhook by ID.**  Unlike the [**Get an Event Webhook**](https://docs.sendgrid.com/api-reference/webhooks/get-an-event-webhook) and [**Update an Event Webhook**](https://docs.sendgrid.com/api-reference/webhooks/update-an-event-webhook) endpoints, which will operate on your oldest webhook by `created_date` when you don't provide an ID, this endpoint will return an error if you do not pass it an ID. This behavior prevents customers from uninten...

---
