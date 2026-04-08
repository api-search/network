---
aid: sendgrid:sendgrid-updatesignedeventwebhook
name: Toggle signature verification for a single Event Webhook by ID
tags:
- Event Webhook
humanURL: 
properties: []
description: >-
  **This endpoint allows you to enable or disable signature verification for a single Event Webhook by ID.**  If you do not pass a webhook ID to this endpoint, it will enable signature verification for your oldest webhook by `created_date`. This means the default webhook operated on by this endpoint when no ID is provided will be the first one you created. This functionality allows customers who do not have multiple webhooks to enable or disable signature verifiction for their only webhook, eve...

---
