---
description: Represents the upload session for iterative file upload.
layout: schema
name: UploadSession
properties_list:
- description: The URL endpoint that accepts PUT requests for byte ranges of the file.
  name: uploadUrl
  type: string
- description: The date and time in UTC that the upload session will expire.
  name: expirationDateTime
  type: string
- description: A collection of byte ranges that the server is missing for the file, such as "0-25", "128-500".
  name: nextExpectedRanges
  type: array
provider_name: Microsoft Outlook
provider_slug: microsoft-outlook
schema_file: json-schema/microsoft-graph-mail-upload-session-schema.json
slug: microsoft-graph-mail-upload-session
tags:
- Calendar
- Contacts
- Email
- Enterprise
- Microsoft
- Office 365
- Productivity
title: UploadSession
---
