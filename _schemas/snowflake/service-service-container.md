---
description: ''
layout: schema
name: ServiceContainer
properties_list:
- description: The current status of the service.
  name: service_status
  type: string
- description: ID of the service instance (this is the index of the service instance starting from 0).
  name: instance_id
  type: string
- description: The current status of the service instance.
  name: instance_status
  type: string
- description: Name of the container.
  name: container_name
  type: string
- description: Service container status.
  name: status
  type: string
- description: Additional clarification about status.
  name: message
  type: string
- description: Image name used to create the service container.
  name: image_name
  type: string
- description: The unique and immutable identifier representing the image content.
  name: image_digest
  type: string
- description: Number of times Snowflake restarted the service.
  name: restart_count
  type: integer
- description: Date and time when the container started.
  name: start_time
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/service-service-container-schema.json
slug: service-service-container
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: ServiceContainer
---
