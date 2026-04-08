---
aid: sendgrid:sendgrid-listemailjobforverification
name: Request a presigned URL and headers for Bulk Email Address Validation list upload.
tags:
- Bulk Email Address Validation
humanURL: 
properties: []
description: >-
  **This endpoint returns a presigned URL and request headers. Use this information to upload a list of email addresses for verification.**  Note that in a successful response the `content-type` header value matches the provided `file_type` parameter in the `PUT` request.  Once you have an `upload_uri` and the `upload_headers`, you're ready to upload your email address list for verification. For the expected format of the email address list and a sample upload request, see the [Bulk Email Addre...

---
