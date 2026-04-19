---
description: Project schema from Ampersand API
layout: schema
name: Project
properties_list:
- description: The unique identifier for the project.
  name: id
  type: string
- description: The unique name for the project.
  name: name
  type: string
- description: The display name of the application, shown to end users during the connection flow.
  name: appName
  type: string
- description: The ID of the organization that this project belongs to.
  name: orgId
  type: string
- description: The time the project was created.
  name: createTime
  type: string
- description: The time the project was updated.
  name: updateTime
  type: string
- description: Plan-based feature flags for the project. These are managed by Ampersand and cannot be set via the API.
  name: entitlements
  type: object
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-project-schema.json
slug: ampersand-api-project
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: Project
---
