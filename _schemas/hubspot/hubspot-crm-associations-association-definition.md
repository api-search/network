---
description: Definition of an association type between two object types
layout: schema
name: AssociationDefinition
properties_list:
- description: Unique identifier for the association definition
  name: id
  type: string
- description: Source object type ID
  name: fromObjectTypeId
  type: string
- description: Target object type ID
  name: toObjectTypeId
  type: string
- description: Name of the association type
  name: name
  type: string
- description: Display label for the association
  name: label
  type: string
- description: Label for the inverse association
  name: inverseLabel
  type: string
- description: Category of the association definition
  name: category
  type: string
provider_name: HubSpot
provider_slug: hubspot
schema_file: json-schema/hubspot-crm-associations-association-definition-schema.json
slug: hubspot-crm-associations-association-definition
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Operations
- Sales
title: AssociationDefinition
---
