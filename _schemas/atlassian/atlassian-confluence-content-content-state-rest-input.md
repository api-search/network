---
description: ''
layout: schema
name: ContentStateRestInput
properties_list:
- description: Name of content state. Maximum 20 characters.
  name: name
  type: string
- description: 'Color of state. Must be in 6 digit hex form (#FFFFFF). The default colors offered in the UI are: #ff7452 (red), #2684ff (blue), #ffc400 (yellow), #57d9a3 (green), and #8777d9 (purple)'
  name: color
  type: string
- description: id of state. This can be 0,1, or 2 if you wish to specify a default space state.
  name: id
  type: integer
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-confluence-content-content-state-rest-input-schema.json
slug: atlassian-confluence-content-content-state-rest-input
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: ContentStateRestInput
---
