---
aid: atlassian:atlassian-updateattachmentdata
name: Update Attachment Data
tags:
- Update
- Attachments
- Data
humanURL: 
properties: []
description: >-
  Updates the binary data of an existing attachment in Confluence by uploading a new file to replace the current attachment content. This operation requires the attachment ID and content ID as path parameters, and the new file data must be sent as multipart/form-data in the request body. The endpoint maintains the attachment's metadata such as title and file extension while replacing only the actual file content. Upon successful update, it returns the updated attachment object with new version ...

---
