---
aid: sendgrid:sendgrid-exportrecipient
name: Export Recipients
tags:
- Recipients
humanURL: 
properties: []
description: >-
  **Use this endpoint to export lists or segments of recipients**.  If you would just like to have a link to the exported list sent to your email set the `notifications.email` option to `true` in the `POST` payload.  If you would like to download the list, take the `id` that is returned and use the "Export Recipients Status" endpoint to get the `urls`. Once you have the list of URLs, make a `GET` request to each URL provided to download your CSV file(s).  You specify the segments and or/recipie...

---
