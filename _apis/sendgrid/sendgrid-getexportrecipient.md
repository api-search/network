---
aid: sendgrid:sendgrid-getexportrecipient
name: Export Recipients Status
tags:
- Recipients
humanURL: 
properties: []
description: >-
  **This endpoint can be used to check the status of a recipient export job**.   To use this call, you will need the `id` from the "Export Recipients" call.  If you would like to download a list, take the `id` that is returned from the "Export Recipients" endpoint and make an API request here to get the `urls`. Once you have the list of URLs, make a `GET` request on each URL to download your CSV file(s).  Twilio SendGrid recommends exporting your recipients regularly as a backup to avoid issues...

---
