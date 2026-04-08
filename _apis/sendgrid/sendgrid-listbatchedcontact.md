---
aid: sendgrid:sendgrid-listbatchedcontact
name: Get Batched Contacts by IDs
tags:
- Contacts
humanURL: 
properties: []
description: >-
  **This endpoint is used to retrieve a set of contacts identified by their IDs.**  This can be more efficient endpoint to get contacts than making a series of individual `GET` requests to the "Get a Contact by ID" endpoint.  You can supply up to 100 IDs. Pass them into the `ids` field in your request body as an array or one or more strings.  Twilio SendGrid recommends exporting your contacts regularly as a backup to avoid issues or lost data.

---
