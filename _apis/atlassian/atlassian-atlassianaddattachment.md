---
aid: atlassian:atlassian-atlassianaddattachment
name: Add Attachment
tags:
- Issue attachments
humanURL: 
properties: []
description: >-
  Adds one or more attachments to an issue. Attachments are posted as multipart/form-data ([RFC 1867](https://www.ietf.org/rfc/rfc1867.txt)).<br><br>Note that:<br><br> *  The request must have a `X-Atlassian-Token: no-check` header, if not it is blocked. See [Special headers](#special-request-headers) for more information.<br> *  The name of the multipart/form-data parameter that contains the attachments must be `file`.<br><br>The following examples upload a file called *myfile.txt* to the issu...

---
