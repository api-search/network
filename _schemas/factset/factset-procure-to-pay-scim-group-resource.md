---
description: ''
layout: schema
name: GroupResource
properties_list:
- description: ''
  name: schemas
  type: array
- description: ''
  name: id
  type: string
- description: ''
  name: externalId
  type: string
- description: A human-readable name for the Group.
  name: displayName
  type: string
- description: A description for the Group.
  name: description
  type: string
- description: A list of members of the Group.
  name: members
  type: array
- description: ''
  name: urn:scim:schemas:extension:FactSet:EnterpriseHosting:1.0:Group
  type: object
- description: ''
  name: urn:scim:schemas:extension:FactSet:VRS:1.0:Group
  type: object
- description: ''
  name: meta
  type: object
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-procure-to-pay-scim-group-resource-schema.json
slug: factset-procure-to-pay-scim-group-resource
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: GroupResource
---
