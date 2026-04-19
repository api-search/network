---
description: Basic information about a person entity.
layout: schema
name: profile
properties_list:
- description: Person identifier used in the request.
  name: requestId
  type: string
- description: FactSet Entity Identifier for the Person
  name: personId
  type: string
- description: Last Name
  name: lastName
  type: string
- description: Name
  name: factsetName
  type: string
- description: First Name
  name: firstName
  type: string
- description: Middle Name
  name: middleName
  type: string
- description: Formal Name
  name: formalName
  type: string
- description: Proper Name
  name: properName
  type: string
- description: Primary Salutation of Name
  name: salutation
  type: string
- description: The Highest Held Degree Code.
  name: highestDegree
  type: string
- description: The Highest Degree Institution Name.
  name: highestDegreeInst
  type: string
- description: Suffix of Name
  name: suffix
  type: string
- description: Person's age in years.
  name: age
  type: number
- description: Person's Gender.
  name: gender
  type: string
- description: Most Recent Salary
  name: salary
  type: number
- description: Most Recent Total Compensation
  name: totalCompensation
  type: number
- description: Entity identifier of primary `Company` of employment.
  name: primaryCompanyId
  type: string
- description: Name of primary company of employment
  name: primaryCompanyName
  type: string
- description: Title at primary `Company` of employment
  name: primaryTitle
  type: string
- description: Brief biography of the person requested.
  name: biography
  type: string
provider_name: Factset
provider_slug: factset
schema_file: json-schema/factset-people-profile-schema.json
slug: factset-people-profile
tags:
- Financial
- Financial Data
- Investment Analytics
- Market Data
- Portfolio Analytics
- Research
title: profile
---
