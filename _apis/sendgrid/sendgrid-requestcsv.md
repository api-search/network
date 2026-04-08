---
aid: sendgrid:sendgrid-requestcsv
name: Request CSV
tags:
- Email Activity
humanURL: 
properties: []
description: >-
  This request will kick off a backend process to generate a CSV file. Once generated, the worker will then send an email for the user download the file. The link will expire in 3 days.  The CSV will contain the events from the last 30 days, limited to the last 1 million events maximum. This endpoint will be rate limited to 1 request every 12 hours (rate limit may change).  This endpoint is similar to the GET Single Message endpoint - the only difference is that /download is added to indicate t...

---
