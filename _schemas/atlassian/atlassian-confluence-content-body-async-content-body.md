---
description: ''
layout: schema
name: AsyncContentBody
properties_list:
- description: ''
  name: value
  type: string
- description: ''
  name: representation
  type: string
- description: ''
  name: renderTaskId
  type: string
- description: ''
  name: error
  type: string
- description: Rerunning is reserved for when the job is working, but there is a previous run's value in the cache. You may choose to continue polling, or use the cached value.
  name: status
  type: string
- description: ''
  name: embeddedContent
  type: array
- description: ''
  name: mediaToken
  type: object
- description: ''
  name: _expandable
  type: object
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-confluence-content-body-async-content-body-schema.json
slug: atlassian-confluence-content-body-async-content-body
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: AsyncContentBody
---
