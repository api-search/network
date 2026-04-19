---
description: Represents an organization-level policy that defines rules and controls for security, authentication, and governance.
layout: schema
name: Policy
properties_list:
- description: The unique identifier of the policy.
  name: id
  type: string
- description: The type of policy.
  name: type
  type: string
- description: The display name of the policy.
  name: name
  type: string
- description: The current status of the policy.
  name: status
  type: string
- description: Policy-specific configuration attributes.
  name: attributes
  type: object
- description: Resources this policy applies to.
  name: resources
  type: array
- description: When the policy was created.
  name: created
  type: string
- description: When the policy was last updated.
  name: updated
  type: string
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-admin-policy-schema.json
slug: atlassian-admin-policy
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: Policy
---
