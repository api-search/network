---
aid: npr:npr-revoketoken
name: NPR Revoke an existing OAuth2 access token
tags:
- Authorization
humanURL: 
properties: []
description: >-
  Our implementation follows the proposed IETF specification [RFC-7009](https://tools.ietf.org/html/rfc7009).  If your client application offers the ability to for a logged-in user to log out, and you have access to a long-lived `client_credentials` token (i.e. you have generated one that you are storing securely for the lifetime of the entire app install), we suggest (but do not require) that you call this endpoint and revoke the access token belonging to the logged-in user as part of your log...

---
