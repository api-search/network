---
description: ScimPatchRequest schema from Amplitude SCIM API
layout: schema
name: ScimPatchRequest
properties_list:
- description: The SCIM patch operation schema URI, typically urn:ietf:params:scim:api:messages:2.0:PatchOp.
  name: schemas
  type: array
- description: Array of patch operations to apply.
  name: Operations
  type: array
provider_name: Amplitude
provider_slug: amplitude
schema_file: json-schema/scim-api-scim-patch-request-schema.json
slug: scim-api-scim-patch-request
tags:
- A/B Testing
- Analytics
- Experimentation
- Feature Flags
- Product Analytics
- User Behavior
title: ScimPatchRequest
---
