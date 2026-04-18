---
description: A Cosmos DB database resource.
layout: schema
name: Database
properties_list:
- description: The unique name that identifies the database.
  name: id
  type: string
- description: System-generated resource ID.
  name: _rid
  type: string
- description: System-generated timestamp (epoch value).
  name: _ts
  type: integer
- description: System-generated URI for the resource.
  name: _self
  type: string
- description: System-generated resource etag for optimistic concurrency.
  name: _etag
  type: string
- description: System-generated addressable path for the collections resource.
  name: _colls
  type: string
- description: System-generated addressable path for the users resource.
  name: _users
  type: string
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-cosmos-db-database-schema.json
slug: azure-cosmos-db-database
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: Database
---
