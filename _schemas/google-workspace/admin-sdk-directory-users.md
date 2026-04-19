---
description: A paginated list of user resources.
layout: schema
name: Users
properties_list:
- description: The type of the API resource.
  name: kind
  type: string
- description: ETag of the resource.
  name: etag
  type: string
- description: A list of user objects.
  name: users
  type: array
- description: Token for retrieving the next page of results.
  name: nextPageToken
  type: string
- description: Event that triggered this response (for push notifications).
  name: trigger_event
  type: string
provider_name: Google Workspace
provider_slug: google-workspace
schema_file: json-schema/admin-sdk-directory-users-schema.json
slug: admin-sdk-directory-users
tags:
- Calendar
- Collaboration
- Email
- Productivity
- Storage
- Video Conferencing
title: Users
---
