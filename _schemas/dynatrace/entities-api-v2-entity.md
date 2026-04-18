---
description: Represents a monitored entity in Dynatrace. Entities are the components of your monitored environment such as services, hosts, processes, and applications. Each entity has a unique ID, a type, properties, tags, and relationships to other entities.
layout: schema
name: Entity
properties_list:
- description: The unique identifier of the entity in the format TYPE-HEXADECIMALID, e.g., SERVICE-1234567890ABCDEF.
  name: entityId
  type: string
- description: The human-readable display name of the entity.
  name: displayName
  type: string
- description: The type of the entity, e.g., SERVICE, HOST, PROCESS_GROUP, APPLICATION, SYNTHETIC_TEST.
  name: type
  type: string
- description: The Unix timestamp in milliseconds when the entity was first seen.
  name: firstSeenTms
  type: integer
- description: The Unix timestamp in milliseconds when the entity was last seen.
  name: lastSeenTms
  type: integer
- description: A map of entity-type-specific properties. Available properties vary by entity type. For example, a HOST entity may include osType, cpuCores, and memoryTotalBytes.
  name: properties
  type: object
- description: The list of tags applied to the entity, including auto-detected and manually defined tags.
  name: tags
  type: array
- description: The management zones that the entity belongs to, used for access control and organizational scoping.
  name: managementZones
  type: array
- description: 'Relationships where this entity is the target. Keys are relationship types (e.g., isProcessOf), values are arrays of entity IDs. For example, {"isProcessOf": ["PROCESS_GROUP-123"]}.'
  name: toRelationships
  type: object
- description: 'Relationships where this entity is the source. Keys are relationship types (e.g., runsOn), values are arrays of entity IDs. For example, {"runsOn": ["HOST-456"]}.'
  name: fromRelationships
  type: object
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/entities-api-v2-entity-schema.json
slug: entities-api-v2-entity
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
title: Entity
---
