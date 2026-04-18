---
description: A Jira user.
layout: schema
name: UserDetails
properties_list:
- description: The URL of the user in the REST API.
  name: self
  type: string
- description: The account ID of the user, which uniquely identifies the user across all Atlassian products.
  name: accountId
  type: string
- description: The email address of the user (may not be available depending on privacy settings).
  name: emailAddress
  type: string
- description: The display name of the user.
  name: displayName
  type: string
- description: Whether the user account is active.
  name: active
  type: boolean
- description: The time zone of the user.
  name: timeZone
  type: string
- description: The type of account.
  name: accountType
  type: string
provider_name: Jira
provider_slug: jira
schema_file: json-schema/jira-cloud-platform-rest-user-details-schema.json
slug: jira-cloud-platform-rest-user-details
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
title: UserDetails
---
