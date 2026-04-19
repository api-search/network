---
description: Request body for updating a policy.
layout: schema
name: PolicyUpdateRequest
properties_list:
- description: The updated display name for the policy.
  name: name
  type: string
- description: The updated status for the policy.
  name: status
  type: string
- description: Updated policy-specific configuration attributes.
  name: attributes
  type: object
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-admin-policy-update-request-schema.json
slug: atlassian-admin-policy-update-request
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: PolicyUpdateRequest
---
