---
description: A monitored entity that is impacted by the problem.
layout: schema
name: ImpactedEntity
properties_list:
- description: The Dynatrace entity ID of the impacted entity, in the format TYPE-HEXADECIMALID, e.g., SERVICE-1234567890ABCDEF.
  name: Entity
  type: string
- description: The display name of the impacted entity.
  name: Name
  type: string
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/problems-impacted-entity-schema.json
slug: problems-impacted-entity
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
title: ImpactedEntity
---
