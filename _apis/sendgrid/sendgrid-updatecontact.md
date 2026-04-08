---
aid: sendgrid:sendgrid-updatecontact
name: Add or Update a Contact
tags:
- Contacts
humanURL: 
properties: []
description: >-
  **This endpoint allows the [upsert](https://en.wiktionary.org/wiki/upsert) (insert or update) of up to 30,000 contacts, or 6MB of data, whichever is lower**. Because the creation and update of contacts is an asynchronous process, the response will not contain immediate feedback on the processing of your upserted contacts. Rather, it will contain an HTTP 202 response indicating the contacts are queued for processing or an HTTP 4XX error containing validation errors. Should you wish to get the ...

---
