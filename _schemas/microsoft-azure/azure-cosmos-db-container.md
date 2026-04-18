---
description: A Cosmos DB container (collection) resource.
layout: schema
name: Container
properties_list:
- description: The unique name that identifies the container.
  name: id
  type: string
- description: Default time-to-live in seconds. -1 means items never expire.
  name: defaultTtl
  type: integer
- description: System-generated resource ID.
  name: _rid
  type: string
- description: System-generated timestamp.
  name: _ts
  type: integer
- description: System-generated URI for the resource.
  name: _self
  type: string
- description: System-generated resource etag.
  name: _etag
  type: string
- description: Addressable path for the documents resource.
  name: _docs
  type: string
- description: Addressable path for the stored procedures resource.
  name: _sprocs
  type: string
- description: Addressable path for the triggers resource.
  name: _triggers
  type: string
- description: Addressable path for the user-defined functions resource.
  name: _udfs
  type: string
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-cosmos-db-container-schema.json
slug: azure-cosmos-db-container
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: Container
---
