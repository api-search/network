---
aid: sendgrid:sendgrid-listsubuserassignedtoip
name: Get a List of Subusers Assigned to an IP
tags:
- IP Address Management
humanURL: 
properties: []
description: >-
  This operation returns a list of Subuser IDs that have been assigned the specified IP address. To retrieve more information about the returned Subusers, use the [Subusers API](https://docs.sendgrid.com/api-reference/subusers-api/list-all-subusers).  You can use the `after_key` and `limit` query parameters to iterate through paginated results. The maximum limit is 100, meaning you may retrieve up to 100 Subusers per request. If the `after_key` in the API response is not null, there are more Su...

---
