---
aid: sendgrid:sendgrid-getexportcontact
name: Export Contacts Status
tags:
- Contacts
humanURL: 
properties: []
description: >-
  **This endpoint can be used to check the status of a contact export job**.   To use this call, you will need the `id` from the "Export Contacts" call.  If you would like to download a list, take the `id` that is returned from the "Export Contacts" endpoint and make an API request here to get the `urls`. Once you have the list of URLs, make a `GET` request on each URL to download your CSV file(s).  Twilio SendGrid recommends exporting your contacts regularly as a backup to avoid issues or lost...

---
