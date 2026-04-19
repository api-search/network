---
description: Entity Match object showing the decision reached for each Entity.
layout: schema
name: EntityMatch
properties_list:
- description: FactSet Entity Identifier of the entity matched respective to the requested Name submitted. For more detail, visit [FactSet Permanent Security Identifier](https://oa.apps.factset.com/cms/oaAttachment/
  name: entityId
  type: string
- description: Full name corresponding to the matched entity.
  name: entityName
  type: string
- description: ISO2 country code corresponding to the location of the matched entity.
  name: countryCode
  type: string
- description: Code representing the entity type of the matched entity. See the related request parameter for a table of all Codes and their respective descriptions.
  name: entityTypeCode
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-private-markets-entity-match-schema.json
slug: factset-private-markets-entity-match
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: EntityMatch
---
