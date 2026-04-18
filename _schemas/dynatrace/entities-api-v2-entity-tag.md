---
description: A tag applied to a monitored entity.
layout: schema
name: EntityTag
properties_list:
- description: The origin context of the tag. For example, CONTEXTLESS, ENVIRONMENT, AWS, KUBERNETES, etc.
  name: context
  type: string
- description: The key of the tag.
  name: key
  type: string
- description: The value of the tag, if applicable.
  name: value
  type: string
- description: The full string representation of the tag as displayed in the Dynatrace UI, e.g., [KUBERNETES]app:my-service.
  name: stringRepresentation
  type: string
provider_name: Dynatrace
provider_slug: dynatrace
schema_file: json-schema/entities-api-v2-entity-tag-schema.json
slug: entities-api-v2-entity-tag
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
title: EntityTag
---
