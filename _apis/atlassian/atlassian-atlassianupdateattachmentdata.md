---
aid: atlassian:atlassian-atlassianupdateattachmentdata
name: Update Attachment Data
tags:
- Content - attachments
humanURL: 
properties: []
description: >-
  Updates the binary data of an attachment, given the attachment ID, and<br>optionally the comment and the minor edit field.<br><br>This method is essentially the same as [Create or update attachments](#api-content-id-child-attachment-put),<br>except that it matches the attachment ID rather than the name.<br><br>Note, you must set a `X-Atlassian-Token: nocheck` header on the request<br>for this method, otherwise it will be blocked. This protects against XSRF<br>attacks, which is necessary as th...

---
