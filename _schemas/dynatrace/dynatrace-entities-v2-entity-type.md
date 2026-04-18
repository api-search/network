---
description: Defines an entity type including its display name, available properties, and supported relationship types.
layout: schema
name: EntityType
properties_list:
- description: The entity type identifier, e.g., SERVICE.
  name: type
  type: string
- description: The human-readable display name of the entity type.
  name: displayName
  type: string
- description: A description of what this entity type represents.
  name: description
  type: string
- description: The list of properties available for this entity type.
  name: properties
  type: array
- description: The relationship types where entities of this type are the source.
  name: fromRelationships
  type: array
- description: The relationship types where entities of this type are the target.
  name: toRelationships
  type: array
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/dynatrace-entities-v2-entity-type-schema.json
slug: dynatrace-entities-v2-entity-type
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
title: EntityType
---
