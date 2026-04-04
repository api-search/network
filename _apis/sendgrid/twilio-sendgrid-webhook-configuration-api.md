---
aid: sendgrid:twilio-sendgrid-webhook-configuration-api
name: Twilio SendGrid Webhook Configuration API
tags: []
properties:
  - url: openapi/tsg_webhooks_v3.yaml
    type: OpenAPI
description: >-
  The Twilio SendGrid Webhooks API allows you to configure the Event and Parse
  Webhooks.


  Email is a data-rich channel, and implementing the Event Webhook will allow
  you to consume those data in nearly real time. This means you can actively
  monitor and participate in the health of your email program throughout the
  send cycle.


  The Inbound Parse Webhook processes all incoming email for a domain or
  subdomain, parses the contents and attachments and then POSTs
  `multipart/form-data` to a URL that you choose. 

---