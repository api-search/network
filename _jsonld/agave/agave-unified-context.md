---
class_count: 24
classes:
- EmployeeList
- CostCodeList
- TimesheetList
- Contract
- name
- ContractList
- Budget
- description
- LinkSessionRequest
- VendorList
- LinkSession
- ProjectList
- Timesheet
- BudgetList
- Invoice
- Project
- createdAt
- updatedAt
- Vendor
- email
- Employee
- InvoiceList
- CostCode
- InvoiceRequest
context_file: json-ld/agave-unified-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/agave/refs/heads/main/json-ld/agave-unified-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Agave Unified from Agave.
layout: jsonld
name: Agave Unified Context
namespaces:
- prefix: agave
  uri: https://agave.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: set
  name: data
  type: string
- container: ''
  name: nextCursor
  type: string
- container: ''
  name: count
  type: integer
- container: ''
  name: id
  type: string
- container: ''
  name: projectId
  type: string
- container: ''
  name: number
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: originalValue
  type: decimal
- container: ''
  name: revisedValue
  type: decimal
- container: ''
  name: executedDate
  type: date
- container: ''
  name: costCodeId
  type: string
- container: ''
  name: originalAmount
  type: decimal
- container: ''
  name: revisedAmount
  type: decimal
- container: ''
  name: actualCost
  type: decimal
- container: ''
  name: projectedCost
  type: decimal
- container: ''
  name: referenceId
  type: string
- container: ''
  name: redirectUrl
  type: string
- container: ''
  name: linkToken
  type: string
- container: ''
  name: expiresAt
  type: dateTime
- container: ''
  name: employeeId
  type: string
- container: ''
  name: date
  type: date
- container: ''
  name: regularHours
  type: decimal
- container: ''
  name: overtimeHours
  type: decimal
- container: ''
  name: payRate
  type: decimal
- container: ''
  name: vendorId
  type: string
- container: ''
  name: invoiceNumber
  type: string
- container: ''
  name: amount
  type: decimal
- container: ''
  name: invoiceDate
  type: date
- container: ''
  name: dueDate
  type: date
- container: ''
  name: sourceId
  type: string
- container: ''
  name: address
  type: string
- container: ''
  name: startDate
  type: date
- container: ''
  name: estimatedCompletionDate
  type: date
- container: ''
  name: totalBudget
  type: decimal
- container: ''
  name: phone
  type: string
- container: ''
  name: taxId
  type: string
- container: ''
  name: firstName
  type: string
- container: ''
  name: lastName
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: hireDate
  type: date
- container: ''
  name: code
  type: string
- container: ''
  name: costType
  type: string
property_count: 42
provider_name: Agave
provider_slug: agave
slug: agave-unified-context
tags:
- Accounting
- Construction
- Integration
- JSON-LD
- Linked Data
- Semantic Web
---
