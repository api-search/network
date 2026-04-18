---
description: ''
layout: schema
name: PageCreateRequest
properties_list:
- description: The ID of the space to create the page in.
  name: spaceId
  type: string
- description: The status of the page.
  name: status
  type: string
- description: The title of the page.
  name: title
  type: string
- description: The ID of the parent page. If omitted, the page will be a root-level page.
  name: parentId
  type: string
provider_name: Confluence
provider_slug: confluence
schema_file: json-schema/confluence-cloud-v2-page-create-request-schema.json
slug: confluence-cloud-v2-page-create-request
tags:
- Collaboration
- Content Management
- Documentation
- Knowledge Base
- Wiki
title: PageCreateRequest
---
