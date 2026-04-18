---
description: A query session.
layout: schema
name: Session
properties_list:
- description: Unique session identifier.
  name: sessionId
  type: string
- description: Connected system name.
  name: system
  type: string
- description: Default database.
  name: database
  type: string
- description: Session status.
  name: status
  type: string
- description: Session creation time.
  name: createdAt
  type: string
provider_name: Teradata
provider_slug: teradata
schema_file: json-schema/query-service-api-session-schema.json
slug: query-service-api-session
tags:
- Analytics
- Cloud
- Data Management
- Data Warehousing
- Database
- Enterprise
- Machine Learning
- SQL
title: Session
---
