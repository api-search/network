---
description: The user or group that the permission applies to.
layout: schema
name: PermissionSubjectWithGroupId
properties_list:
- description: ''
  name: type
  type: string
- description: for `type=user`, identifier should be user's accountId or `anonymous` for anonymous users for `type=group`, identifier should be ID of the group
  name: identifier
  type: string
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-confluence-content-permission-subject-with-group-id-schema.json
slug: atlassian-confluence-content-permission-subject-with-group-id
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: PermissionSubjectWithGroupId
---
