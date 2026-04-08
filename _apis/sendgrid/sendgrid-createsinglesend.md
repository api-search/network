---
aid: sendgrid:sendgrid-createsinglesend
name: Create Single Send
tags:
- Single Sends
humanURL: 
properties: []
description: >-
  **This endpoint allows you to create a new Single Send.**  Please note that if you are migrating from the previous version of Single Sends, you no longer need to pass a template ID with your request to this endpoint. Instead, you will pass all template data in the `email_config` object.  This endpoint will create a draft of the Single Send but will not send it or schedule it to be sent. Any `send_at` property value set with this endpoint will prepopulate the Single Send's send date. However, ...

---
