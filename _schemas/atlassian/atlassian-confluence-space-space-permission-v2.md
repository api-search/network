---
description: 'This object represents a single space permission. Permissions consist of at least one operation object with an accompanying subjects object. The following combinations of `operation.key` and `operation.target` values are valid for the `operation` object: ``` bash ''create'': ''page'', ''blogpost'', ''comment'', ''attachment'' ''read'': ''space'' ''delete'': ''page'', ''blogpost'', ''comment'', ''attachment'', ''space'' ''export'': ''space'' ''administer'': ''space'' ''archive'': ''page'' ''restrict_content'': ''space'' ``` For example, to enable Delete Own permission, set the `operation` object to the following: ``` "operation": { "key": "delete", "target": "space" } ``` To enable Add/Delete Restrictions permissions, set the `operation` object to the following: ``` "operation": { "key": "restrict_content", "target": "space" } ```'
layout: schema
name: SpacePermissionV2
properties_list:
- description: ''
  name: id
  type: integer
- description: ''
  name: operation
  type: object
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-confluence-space-space-permission-v2-schema.json
slug: atlassian-confluence-space-space-permission-v2
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: SpacePermissionV2
---
