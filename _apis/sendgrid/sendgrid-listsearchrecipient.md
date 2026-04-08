---
aid: sendgrid:sendgrid-listsearchrecipient
name: Search recipients
tags:
- Recipients
humanURL: 
properties: []
description: >-
  **This endpoint allows you to perform a search on all of your Marketing Campaigns recipients.**  field_name:  * is a variable that is substituted for your actual custom field name from your recipient. * Text fields must be url-encoded. Date fields are searchable only by unix timestamp (e.g. 2/2/2015 becomes 1422835200) * If field_name is a 'reserved' date field, such as created_at or updated_at, the system will internally convert your epoch time to a date range encompassing the entire day. Fo...

---
