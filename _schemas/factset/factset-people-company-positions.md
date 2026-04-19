---
description: List of executives for the specified company identifier.
layout: schema
name: companyPositions
properties_list:
- description: FactSet Identifier for the company.
  name: fsymId
  type: string
- description: Factset Entity Identifier for the Person
  name: personId
  type: string
- description: FactSet Name of the person
  name: name
  type: string
- description: The requested Position Title
  name: title
  type: string
- description: The number of years individual is at firm. For founders, this is since inception.
  name: yearsAtFirm
  type: number
- description: The age of the person requested.
  name: age
  type: number
- description: The Gender of the person requested.
  name: gender
  type: string
- description: The requested position code.
  name: requestPosition
  type: string
- description: Original identifier used for the request.
  name: requestId
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-people-company-positions-schema.json
slug: factset-people-company-positions
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: companyPositions
---
