---
class_count: 13
classes:
- Employee
- Company
- Employment
- Team
- Location
- Benefit
- TimeOff
- TimeOffBalance
- PayGroup
- Group
- BankInfo
- EmployeePayrollRun
- PayrollRun
context_file: json-ld/merge-hris-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/merge/refs/heads/main/json-ld/merge-hris-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Merge Hris Api from Merge.
layout: jsonld
name: Merge Hris Api Context
namespaces:
- prefix: merge
  uri: https://api.merge.dev/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: string
- container: ''
  name: remoteId
  type: string
- container: ''
  name: employeeNumber
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: displayFullName
  type: string
- container: ''
  name: workEmail
  type: string
- container: ''
  name: personalEmail
  type: string
- container: ''
  name: mobilePhoneNumber
  type: string
- container: ''
  name: dateOfBirth
  type: date
- container: ''
  name: startDate
  type: dateTime
- container: ''
  name: terminationDate
  type: dateTime
- container: ''
  name: employmentStatus
  type: string
- container: ''
  name: manager
  type: reference
- container: ''
  name: company
  type: reference
- container: ''
  name: team
  type: reference
- container: ''
  name: payGroup
  type: reference
- container: set
  name: groups
  type: reference
- container: ''
  name: remoteWasDeleted
  type: boolean
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: modifiedAt
  type: dateTime
- container: ''
  name: legalName
  type: string
- container: ''
  name: jobTitle
  type: string
- container: ''
  name: payRate
  type: decimal
- container: ''
  name: payPeriod
  type: string
- container: ''
  name: payCurrency
  type: string
- container: ''
  name: employmentType
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: city
  type: string
- container: ''
  name: state
  type: string
- container: ''
  name: zipCode
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: providerName
  type: string
- container: ''
  name: benefitPlanType
  type: string
- container: ''
  name: employeeContribution
  type: decimal
- container: ''
  name: companyContribution
  type: decimal
- container: ''
  name: balance
  type: decimal
- container: ''
  name: grossPay
  type: decimal
- container: ''
  name: netPay
  type: decimal
property_count: 39
provider_name: Merge
provider_slug: merge
slug: merge-hris-api-context
tags:
- Integrations
- Platform
- Unified API
- JSON-LD
- Linked Data
- Semantic Web
---
