---
description: Relationship information for a field to another object
layout: schema
name: AssociationDefinition
properties_list:
- description: High-level association variety (e.g., 'foreignKey', 'lookup', 'ref')
  name: associationType
  type: string
- description: Name of the referenced/parent object
  name: targetObject
  type: string
- description: Name of the referenced field on the target object
  name: targetField
  type: string
- description: Association cardinality from the referencing field's perspective
  name: cardinality
  type: string
- description: Behavior upon foreign object deletion
  name: onDelete
  type: string
- description: If true, a referenced record must exist
  name: required
  type: boolean
- description: Optional inverse relationship/property name exposed on the target object
  name: reverseLookupFieldName
  type: string
- description: ''
  name: labels
  type: object
provider_name: Ampersand
provider_slug: ampersand
schema_file: json-schema/ampersand-api-association-definition-schema.json
slug: ampersand-api-association-definition
tags:
- Developer Tools
- Integrations
- Platform
- SaaS
- OAuth
- Data Sync
- Webhooks
title: AssociationDefinition
---
