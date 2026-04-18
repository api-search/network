---
description: ''
layout: schema
name: Employee
properties_list:
- description: Person identifier
  name: personId
  type: integer
- description: Employee number
  name: employeeNumber
  type: string
- description: Title (Mr., Mrs., etc.)
  name: title
  type: string
- description: First name
  name: firstName
  type: string
- description: Middle name(s)
  name: middleNames
  type: string
- description: Last name
  name: lastName
  type: string
- description: Full name (derived)
  name: fullName
  type: string
- description: Preferred name
  name: knownAs
  type: string
- description: Email address
  name: emailAddress
  type: string
- description: Gender
  name: sex
  type: string
- description: Date of birth
  name: dateOfBirth
  type: string
- description: National identifier (e.g., SSN)
  name: nationalIdentifier
  type: string
- description: Nationality code
  name: nationality
  type: string
- description: Marital status
  name: maritalStatus
  type: string
- description: Record effective start date (date-tracked)
  name: effectiveStartDate
  type: string
- description: Record effective end date (date-tracked)
  name: effectiveEndDate
  type: string
- description: Original hire date
  name: hireDate
  type: string
- description: ''
  name: currentEmployeeFlag
  type: string
- description: Business group identifier
  name: businessGroupId
  type: integer
- description: ''
  name: addresses
  type: array
- description: ''
  name: phones
  type: array
- description: ''
  name: creationDate
  type: string
- description: ''
  name: lastUpdateDate
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/human-resources-employee-schema.json
slug: human-resources-employee
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: Employee
---
