---
description: An operation and the target entity that it applies to, e.g. create page.
layout: schema
name: OperationCheckResult
properties_list:
- description: The operation itself.
  name: operation
  type: string
- description: The space or content type that the operation applies to. Could be one of- - application - page - blogpost - comment - attachment - space
  name: targetType
  type: string
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-confluence-content-operation-check-result-schema.json
slug: atlassian-confluence-content-operation-check-result
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: OperationCheckResult
---
