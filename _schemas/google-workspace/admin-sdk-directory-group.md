---
description: A Google Workspace group. JSON representation of a group resource from the Admin SDK Directory API.
layout: schema
name: Group
properties_list:
- description: The type of the API resource.
  name: kind
  type: string
- description: The unique ID of a group.
  name: id
  type: string
- description: ETag of the resource.
  name: etag
  type: string
- description: The group email address. This property is required when creating a group. Group email addresses must be unique.
  name: email
  type: string
- description: The group display name.
  name: name
  type: string
- description: An extended description to help users determine the purpose of a group. Maximum 4,096 characters.
  name: description
  type: string
- description: Value is true if this group was created by an administrator rather than a user.
  name: adminCreated
  type: boolean
- description: The number of users that are direct members of the group. Members of child groups are not counted.
  name: directMembersCount
  type: string
- description: A list of a group alias email addresses.
  name: aliases
  type: array
- description: A list of the group non-editable alias email addresses that are outside of the account primary domain or subdomains.
  name: nonEditableAliases
  type: array
provider_name: Google Workspace
provider_slug: google-workspace
schema_file: json-schema/admin-sdk-directory-group-schema.json
slug: admin-sdk-directory-group
tags:
- Calendar
- Collaboration
- Email
- Productivity
- Storage
- Video Conferencing
title: Group
---
