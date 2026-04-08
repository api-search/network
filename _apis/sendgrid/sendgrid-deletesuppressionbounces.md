---
aid: sendgrid:sendgrid-deletesuppressionbounces
name: Delete bounces
tags:
- Bounces
humanURL: 
properties: []
description: >-
  **This endpoint allows you to delete all emails on your bounces list.**  There are two options for deleting bounced emails:   1. You can delete all bounced emails by setting `delete_all` to `true` in the request body.  2. You can delete a selection of bounced emails by specifying the email addresses in the `emails` array of the request body.   **WARNING:** You can not have both `emails` and `delete_all` set.

---
