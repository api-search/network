---
description: Request body for inviting users to the organization.
layout: schema
name: InviteUsersRequest
properties_list:
- description: Email addresses of users to invite.
  name: emails
  type: array
- description: The directory to add the invited users to.
  name: directoryId
  type: string
- description: Groups to assign the invited users to.
  name: groupIds
  type: array
- description: Application roles to assign to the invited users.
  name: roleAssignments
  type: array
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-admin-invite-users-request-schema.json
slug: atlassian-admin-invite-users-request
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: InviteUsersRequest
---
