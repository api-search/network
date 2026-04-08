---
aid: sendgrid:sendgrid-updateforwardspam
name: Update forward spam mail settings
tags:
- Mail Settings
humanURL: 
properties: []
description: >-
  **This endpoint allows you to update your current Forward Spam mail settings.**  Enabling the Forward Spam setting allows you to specify `email` addresses to which spam reports will be forwarded. You can set multiple addresses by passing this endpoint a comma separated list of emails in a single string.  ``` {   "email": "address1@example.com, address2@exapmle.com",   "enabled": true } ```  The Forward Spam setting may also be used to receive emails sent to `abuse@` and `postmaster@` role add...

---
