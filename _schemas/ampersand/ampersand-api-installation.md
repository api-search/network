---
description: Installation schema from Ampersand API
layout: schema
name: Installation
properties_list:
- description: The installation ID.
  name: id
  type: string
- description: The Ampersand project ID.
  name: projectId
  type: string
- description: The integration ID.
  name: integrationId
  type: string
- description: ''
  name: group
  type: object
- description: The health status of the installation.
  name: healthStatus
  type: string
- description: The status of the latest operation for this installation.
  name: lastOperationStatus
  type: string
- description: ''
  name: connection
  type: object
- description: The time the installation was created.
  name: createTime
  type: string
- description: The person who did the installation, in the format of "consumer:{consumer-id}".
  name: createdBy
  type: string
- description: The time the installation was last updated with a new config.
  name: updateTime
  type: string
- description: ''
  name: config
  type: object
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-installation-schema.json
slug: ampersand-api-installation
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: Installation
---
