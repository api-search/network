---
description: Request to list source server lifecycle actions
layout: schema
name: ListSourceServerActionsRequest
properties_list:
- description: Source server ID
  name: sourceServerID
  type: string
- description: Action filters
  name: filters
  type: object
- description: Maximum results to return
  name: maxResults
  type: integer
- description: Pagination token
  name: nextToken
  type: string
- description: Account ID for cross-account access
  name: accountID
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-list-source-server-actions-request-schema.json
slug: application-migration-service-list-source-server-actions-request
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: ListSourceServerActionsRequest
---
