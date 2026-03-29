---
aid: atlassian:atlassian-atlassiancreateattachment
name: Create Attachment
tags:
- Content - attachments
humanURL: 
properties: []
description: >-
  Adds an attachment to a piece of content. This method only adds a new<br>attachment. If you want to update an existing attachment, use<br>[Create or update attachments](#api-content-id-child-attachment-put).<br><br>Note, you must set a `X-Atlassian-Token: nocheck` header on the request<br>for this method, otherwise it will be blocked. This protects against XSRF<br>attacks, which is necessary as this method accepts multipart/form-data.<br><br>The media type 'multipart/form-data' is defined in ...

---
