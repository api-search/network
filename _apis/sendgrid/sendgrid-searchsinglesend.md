---
aid: sendgrid:sendgrid-searchsinglesend
name: Get Single Sends Search
tags:
- Single Sends
humanURL: 
properties: []
description: >-
  **This endpoint allows you to search for Single Sends based on specified criteria.**  You can search for Single Sends by passing a combination of values using the `name`, `status`, and `categories` request body fields.  For example, if you want to search for all Single Sends that are "drafts" or "scheduled" and also associated with the category "shoes," your request body may look like the example below.  ```javascript {   "status": [     "draft",     "scheduled"   ],   "categories": [     "sh...

---
