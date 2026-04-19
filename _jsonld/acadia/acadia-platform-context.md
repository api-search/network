---
class_count: 10
classes:
- WorkInstruction
- description
- WorkInstructionStep
- Employee
- name
- email
- SkillRecord
- EmployeeSkillsMatrix
- Quiz
- Role
context_file: json-ld/acadia-platform-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/acadia/refs/heads/main/json-ld/acadia-platform-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Acadia Platform from Acadia.
layout: jsonld
name: Acadia Platform Context
namespaces:
- prefix: acadia
  uri: https://acadia-software.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: id
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: version
  type: integer
- container: ''
  name: steps
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: updatedAt
  type: dateTime
- container: ''
  name: order
  type: integer
- container: ''
  name: department
  type: string
- container: ''
  name: role
  type: string
- container: ''
  name: trainingCompletion
  type: integer
- container: ''
  name: skillId
  type: string
- container: ''
  name: required
  type: boolean
- container: ''
  name: completed
  type: boolean
- container: ''
  name: completedAt
  type: dateTime
- container: ''
  name: score
  type: integer
- container: ''
  name: employeeId
  type: string
- container: ''
  name: employeeName
  type: string
- container: ''
  name: skills
  type: string
- container: ''
  name: overallCompletion
  type: integer
- container: ''
  name: questionCount
  type: integer
- container: ''
  name: passingScore
  type: integer
- container: ''
  name: requiredTrainings
  type: integer
- container: ''
  name: completionRate
  type: integer
property_count: 25
provider_name: Acadia
provider_slug: acadia
slug: acadia-platform-context
tags:
- Connected Worker
- Knowledge Management
- Manufacturing
- Skills Management
- Training
- Workforce Development
- JSON-LD
- Linked Data
- Semantic Web
---
