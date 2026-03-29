---
aid: atlassian:atlassian-atlassiancreateorupdateattachments
name: Create Or Update Attachment
tags:
- Content - attachments
humanURL: 
properties: []
description: >-
  Adds an attachment to a piece of content. If the attachment already exists<br>for the content, then the attachment is updated (i.e. a new version of the<br>attachment is created).<br><br>Note, you must set a `X-Atlassian-Token: nocheck` header on the request<br>for this method, otherwise it will be blocked. This protects against XSRF<br>attacks, which is necessary as this method accepts multipart/form-data.<br><br>The media type 'multipart/form-data' is defined in [RFC 7578](https://www.ietf....

---
