---
aid: sendgrid:sendgrid-geteventwebhook
name: Get the settings for a single Event Webhook.
tags:
- Event Webhook
humanURL: 
properties: []
description: >-
  **This endpoint allows you to retrieve a single Event Webhook by ID.**  If you do not pass a webhook ID to this endpoint, it will return your oldest webhook by `created_date`. This means the default webhook returned by this endpoint when no ID is provided will be the first one you created. This functionality allows customers who do not have multiple webhooks to use this endpoint to retrieve their only webhook, even if they do not supply an ID. If you have multiple webhooks, you can retrieve t...

---
