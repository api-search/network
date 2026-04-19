---
description: ''
layout: schema
name: ContentRestrictionUpdate
properties_list:
- description: The restriction operation applied to content.
  name: operation
  type: string
- description: The users/groups that the restrictions will be applied to. At least one of `user` or `group` must be specified for this object.
  name: restrictions
  type: object
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-confluence-content-content-restriction-update-schema.json
slug: atlassian-confluence-content-content-restriction-update
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: ContentRestrictionUpdate
---
