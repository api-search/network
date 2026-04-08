---
aid: sendgrid:sendgrid-getmailbatch
name: Validate a batch ID.
tags:
- Mail Batch
humanURL: 
properties: []
description: >-
  **This operation allows you to validate a mail batch ID.**  If you provide a valid batch ID, this operation will return a `200` status code and the batch ID itself. If you provide an invalid batch ID, you will receive a `400` level status code and an error message. A batch ID does not need to be assigned to a send to be considered valid. A successful response means only that the batch ID has been created, but it does not indicate that the ID has been assigned to a send.

---
