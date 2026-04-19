---
description: ''
layout: schema
name: ServiceInstance
properties_list:
- description: The current status of the service.
  name: service_status
  type: string
- description: ID of the service instance (this is the index of the service instance starting from 0).
  name: instance_id
  type: string
- description: The current status of the service instance.
  name: status
  type: string
- description: The unique and immutable identifier that represents the service specification content.
  name: spec_digest
  type: string
- description: The time when Snowflake started creating the service instance.
  name: creation_time
  type: string
- description: The time when Snowflake acknowledged the service instance is running on a node.
  name: start_time
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/service-service-instance-schema.json
slug: service-service-instance
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: ServiceInstance
---
