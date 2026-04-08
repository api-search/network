---
aid: sendgrid:sendgrid-importcontact
name: Import Contacts
tags:
- Contacts
humanURL: 
properties: []
description: >-
  **This endpoint allows a CSV upload containing up to one million contacts or 5GB of data, whichever is smaller. At least one identifier is required for a successful import.**  Imports take place asynchronously: the endpoint returns a URL (`upload_uri`) and HTTP headers (`upload_headers`) which can subsequently be used to `PUT` a file of contacts to be imported into our system.  Uploaded CSV files may also be [gzip-compressed](https://en.wikipedia.org/wiki/Gzip).  In either case, you must incl...

---
