---
description: ''
layout: schema
name: ContentUpdate
properties_list:
- description: The new version for the updated content. Set this to the current version number incremented by one, unless you are changing the status to 'draft' which must have a version number of 1. To get the curr
  name: version
  type: object
- description: The updated title of the content. If you are updating a non-draft `page` or `blogpost`, title is required. If you are not changing the title, set this field to the the current title.
  name: title
  type: string
- description: The type of content. Set this to the current type of the content. For example, - page - blogpost - comment - attachment
  name: type
  type: string
- description: The updated status of the content. Note, if you change the status of a page from 'current' to 'draft' and it has an existing draft, the existing draft will be deleted in favor of the updated page.
  name: status
  type: string
- description: The new parent for the content. Only one parent content 'id' can be specified.
  name: ancestors
  type: array
- description: 'The updated body of the content. Does not apply to attachments. If you are not sure how to generate these formats, you can create a page in the Confluence application, retrieve the content using [Get '
  name: body
  type: object
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-confluence-content-content-update-schema.json
slug: atlassian-confluence-content-content-update
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: ContentUpdate
---
