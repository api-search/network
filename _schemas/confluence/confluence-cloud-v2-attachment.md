---
description: Represents a file attachment on Confluence content.
layout: schema
name: Attachment
properties_list:
- description: The unique identifier of the attachment.
  name: id
  type: string
- description: The status of the attachment.
  name: status
  type: string
- description: The filename of the attachment.
  name: title
  type: string
- description: The MIME type of the attachment.
  name: mediaType
  type: string
- description: Human-readable description of the media type.
  name: mediaTypeDescription
  type: string
- description: Comment associated with the attachment upload.
  name: comment
  type: string
- description: File size in bytes.
  name: fileSize
  type: integer
- description: The web UI link for viewing the attachment.
  name: webuiLink
  type: string
- description: The download link for the attachment.
  name: downloadLink
  type: string
- description: The ID of the page this attachment belongs to.
  name: pageId
  type: string
- description: The ID of the blog post this attachment belongs to.
  name: blogPostId
  type: string
provider_name: Confluence
provider_slug: confluence
schema_file: json-schema/confluence-cloud-v2-attachment-schema.json
slug: confluence-cloud-v2-attachment
tags:
- Collaboration
- Content Management
- Documentation
- Knowledge Base
- Wiki
title: Attachment
---
