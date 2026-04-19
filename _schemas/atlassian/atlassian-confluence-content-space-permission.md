---
description: 'This object represents a permission for given space. Permissions consist of at least one operation object with an accompanying subjects object. The following combinations of `operation` and `targetType` values are valid for the `operation` object: - ''create'': ''page'', ''blogpost'', ''comment'', ''attachment'' - ''read'': ''space'' - ''delete'': ''page'', ''blogpost'', ''comment'', ''attachment'' - ''export'': ''space'' - ''administer'': ''space'''
layout: schema
name: SpacePermission
properties_list:
- description: ''
  name: id
  type: integer
- description: The users and/or groups that the permission applies to.
  name: subjects
  type: object
- description: Grant anonymous users permission to use the operation.
  name: anonymousAccess
  type: boolean
- description: Grants access to unlicensed users from JIRA Service Desk when used with the 'read space' operation.
  name: unlicensedAccess
  type: boolean
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-confluence-content-space-permission-schema.json
slug: atlassian-confluence-content-space-permission
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: SpacePermission
---
