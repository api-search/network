---
description: A paginated list of group resources.
layout: schema
name: Groups
properties_list:
- description: The type of the API resource.
  name: kind
  type: string
- description: ETag of the resource.
  name: etag
  type: string
- description: A list of group objects.
  name: groups
  type: array
- description: Token for retrieving the next page of results.
  name: nextPageToken
  type: string
provider_name: Google Workspace
provider_slug: google-workspace
schema_file: json-schema/admin-sdk-directory-groups-schema.json
slug: admin-sdk-directory-groups
tags:
- Calendar
- Collaboration
- Email
- Productivity
- Storage
- Video Conferencing
title: Groups
---
