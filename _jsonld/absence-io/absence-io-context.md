---
class_count: 9
classes:
- Timespan
- name
- Department
- Location
- ReasonType
- Absence
- User
- email
- Allowance
context_file: json-ld/absence-io-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/absence-io/refs/heads/main/json-ld/absence-io-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Absence Io from Absence.io.
layout: jsonld
name: Absence Io Context
namespaces:
- prefix: absence
  uri: https://absence.io/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: Id
  type: string
- container: ''
  name: hoursPerDay
  type: decimal
- container: ''
  name: daysPerWeek
  type: integer
- container: ''
  name: managerId
  type: string
- container: ''
  name: parentId
  type: string
- container: ''
  name: timezone
  type: string
- container: ''
  name: country
  type: string
- container: ''
  name: color
  type: string
- container: ''
  name: requiresApproval
  type: boolean
- container: ''
  name: affectsAllowance
  type: boolean
- container: ''
  name: assignedToId
  type: string
- container: ''
  name: reasonId
  type: string
- container: ''
  name: approverId
  type: string
- container: ''
  name: start
  type: dateTime
- container: ''
  name: end
  type: dateTime
- container: ''
  name: days
  type: decimal
- container: ''
  name: status
  type: integer
- container: ''
  name: comment
  type: string
- container: ''
  name: departmentId
  type: string
- container: ''
  name: locationId
  type: string
- container: ''
  name: teamId
  type: string
- container: ''
  name: language
  type: string
- container: ''
  name: userId
  type: string
- container: ''
  name: year
  type: integer
- container: ''
  name: allowance
  type: decimal
- container: ''
  name: used
  type: decimal
- container: ''
  name: remaining
  type: decimal
- container: ''
  name: carryover
  type: decimal
property_count: 28
provider_name: Absence.io
provider_slug: absence-io
slug: absence-io-context
tags:
- Absences
- Employees
- Leave Management
- HR
- JSON-LD
- Linked Data
- Semantic Web
---
