---
description: ScimUserListResponse schema from Amplitude SCIM API
layout: schema
name: ScimUserListResponse
properties_list:
- description: The SCIM schema URIs for this response.
  name: schemas
  type: array
- description: The total number of matching users.
  name: totalResults
  type: integer
- description: The 1-based index of the first result.
  name: startIndex
  type: integer
- description: The number of results returned in this page.
  name: itemsPerPage
  type: integer
- description: Array of SCIM user resources.
  name: Resources
  type: array
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/scim-api-scim-user-list-response-schema.json
slug: scim-api-scim-user-list-response
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: ScimUserListResponse
---
