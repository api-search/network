---
description: Metadata about a file attachment stored in ServiceNow.
layout: schema
name: Attachment
properties_list:
- description: Unique identifier for the attachment record.
  name: sys_id
  type: string
- description: The name of the attached file.
  name: file_name
  type: string
- description: The table to which the attachment belongs.
  name: table_name
  type: string
- description: The sys_id of the record to which the file is attached.
  name: table_sys_id
  type: string
- description: The MIME type of the attached file.
  name: content_type
  type: string
- description: The size of the attached file in bytes.
  name: size_bytes
  type: integer
- description: The compressed size of the attached file in bytes.
  name: size_compressed
  type: integer
- description: The URL to download the attachment file content.
  name: download_link
  type: string
- description: The height in pixels if the attachment is an image.
  name: image_height
  type: integer
- description: The width in pixels if the attachment is an image.
  name: image_width
  type: integer
- description: The MD5 hash of the file content.
  name: hash
  type: string
- description: The state of the attachment processing.
  name: state
  type: string
- description: The date and time the attachment was created.
  name: sys_created_on
  type: string
- description: The user who uploaded the attachment.
  name: sys_created_by
  type: string
- description: The date and time the attachment was last modified.
  name: sys_updated_on
  type: string
- description: The user who last modified the attachment record.
  name: sys_updated_by
  type: string
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-attachment-attachment-schema.json
slug: servicenow-attachment-attachment
tags:
- Automation
- Cloud Services
- Digital Workflows
- Enterprise Platform
- IT Service Management
- ITSM
- Processes
- T1
- Workflow Automation
- Workflows
title: Attachment
---
