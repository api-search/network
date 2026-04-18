---
description: A reference to a monitored entity in problem details.
layout: schema
name: EntityRef
properties_list:
- description: The unique Dynatrace entity ID.
  name: entityId
  type: string
- description: The display name of the entity.
  name: name
  type: string
- description: The entity type, e.g., SERVICE, HOST, PROCESS_GROUP.
  name: type
  type: string
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/problems-entity-ref-schema.json
slug: problems-entity-ref
tags:
- AI Operations
- Analytics
- APM
- Application Performance Monitoring
- Application Security
- Automation
- Cloud Monitoring
- Digital Experience Management
- Intelligence
- Observability
title: EntityRef
---
