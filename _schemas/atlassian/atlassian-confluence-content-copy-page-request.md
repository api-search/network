---
description: ''
layout: schema
name: CopyPageRequest
properties_list:
- description: If set to `true`, attachments are copied to the destination page.
  name: copyAttachments
  type: boolean
- description: If set to `true`, page permissions are copied to the destination page.
  name: copyPermissions
  type: boolean
- description: If set to `true`, content properties are copied to the destination page.
  name: copyProperties
  type: boolean
- description: If set to `true`, labels are copied to the destination page.
  name: copyLabels
  type: boolean
- description: If set to `true`, custom contents are copied to the destination page.
  name: copyCustomContents
  type: boolean
- description: If defined, this will replace the title of the destination page.
  name: pageTitle
  type: string
- description: If defined, this will replace the body of the destination page.
  name: body
  type: object
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-confluence-content-copy-page-request-schema.json
slug: atlassian-confluence-content-copy-page-request
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: CopyPageRequest
---
