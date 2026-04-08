---
aid: sendgrid:sendgrid-getsignedeventwebhook
name: Get Signed Event Webhook's Public Key
tags:
- Event Webhook
humanURL: 
properties: []
description: >-
  **This endpoint allows you to retrieve the public key for a single Event Webhook by ID.**  If you do not pass a webhook ID to this endpoint, it will return the public key for your oldest webhook by `created_date`. This means the default key returned by this endpoint when no ID is provided will be for the first webhook you created. This functionality allows customers who do not have multiple webhooks to use this endpoint to retrieve their only webhook's public key, even if they do not supply a...

---
