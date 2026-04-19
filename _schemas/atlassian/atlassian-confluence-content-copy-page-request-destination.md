---
description: 'Defines where the page will be copied to, and can be one of the following types. - `parent_page`: page will be copied as a child of the specified parent page - `space`: page will be copied to the specified space as a root page on the space - `existing_page`: page will be copied and replace the specified page'
layout: schema
name: CopyPageRequestDestination
properties_list:
- description: ''
  name: type
  type: string
- description: The space key for `space` type, and content id for `parent_page` and `existing_page`
  name: value
  type: string
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-confluence-content-copy-page-request-destination-schema.json
slug: atlassian-confluence-content-copy-page-request-destination
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: CopyPageRequestDestination
---
