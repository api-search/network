---
description: 'This object represents the response for the content permission check API. If the user or group does not have permissions, the following errors may be returned: - Group does not have permission to the space - Group does not have permission to the content - User is not allowed to use Confluence - User does not have permission to the space - User does not have permission to the content - Anonymous users are not allowed to use Confluence - Anonymous user does not have permission to the space - Anonymous user does not have permission to the content'
layout: schema
name: PermissionCheckResponse
properties_list:
- description: ''
  name: hasPermission
  type: boolean
- description: ''
  name: errors
  type: array
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-confluence-content-permission-check-response-schema.json
slug: atlassian-confluence-content-permission-check-response
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: PermissionCheckResponse
---
