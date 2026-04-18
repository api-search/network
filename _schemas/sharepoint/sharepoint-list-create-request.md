---
description: Request to create a new SharePoint list.
layout: schema
name: ListCreateRequest
properties_list:
- description: ''
  name: __metadata
  type: object
- description: ''
  name: Title
  type: string
- description: ''
  name: Description
  type: string
- description: 100=Generic List, 101=Document Library, 104=Announcements
  name: BaseTemplate
  type: integer
- description: ''
  name: AllowContentTypes
  type: boolean
- description: ''
  name: ContentTypesEnabled
  type: boolean
provider_name: Microsoft SharePoint
provider_slug: sharepoint
schema_file: json-schema/sharepoint-list-create-request-schema.json
slug: sharepoint-list-create-request
tags:
- Collaboration
- Document Management
- Enterprise Content Management
- Intranet
- Microsoft
title: ListCreateRequest
---
