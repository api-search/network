---
aid: sendgrid:sendgrid-updatesender
name: Update a Sender
tags:
- Senders
humanURL: 
properties: []
description: >-
  **This endpoint allows you to update an existing Sender.**  Updates to `from.email` require re-verification. If your domain has been authenticated, a new Sender will auto verify on creation. Otherwise, an email will be sent to the `from.email`.  Partial updates are allowed, but fields that are marked as "required" in the `POST` (create) endpoint must not be nil if that field is included in the `PATCH` request.

---
