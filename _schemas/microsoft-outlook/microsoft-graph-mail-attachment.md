---
description: Base resource for file, item, and reference attachments. Use the @odata.type property to specify the derived type.
layout: schema
name: Attachment
properties_list:
- description: 'The OData type of the attachment. Use #microsoft.graph.fileAttachment for file attachments or #microsoft.graph.itemAttachment for item attachments.'
  name: '@odata.type'
  type: string
- description: The unique identifier of the attachment. Read-only.
  name: id
  type: string
- description: The display name of the attachment.
  name: name
  type: string
- description: The MIME type of the attachment.
  name: contentType
  type: string
- description: The length of the attachment in bytes.
  name: size
  type: integer
- description: True if the attachment is an inline attachment.
  name: isInline
  type: boolean
- description: The date and time the attachment was last modified in UTC.
  name: lastModifiedDateTime
  type: string
- description: The base64-encoded contents of the file. Only applicable for fileAttachment.
  name: contentBytes
  type: string
- description: The ID of the attachment in the Exchange store. Only applicable for fileAttachment.
  name: contentId
  type: string
- description: The Uniform Resource Identifier (URI) corresponding to the location of the content of the attachment.
  name: contentLocation
  type: string
provider_name: Microsoft Outlook
provider_slug: microsoft-outlook
schema_file: json-schema/microsoft-graph-mail-attachment-schema.json
slug: microsoft-graph-mail-attachment
tags:
- Calendar
- Contacts
- Email
- Enterprise
- Microsoft
- Office 365
- Productivity
title: Attachment
---
