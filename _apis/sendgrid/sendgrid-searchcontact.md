---
aid: sendgrid:sendgrid-searchcontact
name: Search Contacts
tags:
- Contacts
humanURL: 
properties: []
description: >-
  **Use this endpoint to locate contacts**.  The request body's `query` field accepts valid [SGQL](https://sendgrid.com/docs/for-developers/sending-email/segmentation-query-language/) for searching for a contact.  Because contact emails are stored in lower case, using SGQL to search by email address requires the provided email address to be in lower case. The SGQL `lower()` function can be used for this.  Only the first 50 contacts that meet the search criteria will be returned.  If the query t...

---
