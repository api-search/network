---
aid: sendgrid:sendgrid-testeventwebhook
name: Test an Event Webhook's settings
tags:
- Event Webhook
humanURL: 
properties: []
description: >-
  **This endpoint allows you to test an Event Webhook.**  Retry logic for this endpoint differs from other endpoints, which use a rolling 24-hour retry.  This endpoint will make a POST request with a fake event notification to a URL you provide. This allows you to verify that you have properly configured the webhook before sending real data to your URL.  ### Test OAuth configuration  To test your OAuth configuration, you must include the necessary OAuth properties: `oauth_client_id`, `oauth_cli...

---
