---
description: List of executives for the specified company identifier.
layout: schema
name: companyPeople
properties_list:
- description: FactSet Identifier for the company requested.
  name: fsymId
  type: string
- description: Email of the person
  name: email
  type: string
- description: FactSet Name of the person
  name: name
  type: string
- description: Job Function1
  name: jobFunction1
  type: string
- description: Job Function2
  name: jobFunction2
  type: string
- description: Job Function3
  name: jobFunction3
  type: string
- description: Job Function4
  name: jobFunction4
  type: string
- description: Main Phone Numbers of the executives.
  name: mainPhone
  type: string
- description: FactSet Entity Identifier for the Person.
  name: personId
  type: string
- description: Phone number of the executives.
  name: phone
  type: string
- description: Original identifier used for the request.
  name: requestId
  type: string
- description: Executive titles for a specified company.
  name: title
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-people-company-people-schema.json
slug: factset-people-company-people
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: companyPeople
---
