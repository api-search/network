---
class_count: 11
classes:
- Project
- Task
- EnterpriseResource
- Assignment
- Calendar
- CustomField
- LookupTable
- TimeSheet
- Phase
- Stage
- EnterpriseProjectType
context_file: json-ld/microsoft-project-rest-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/microsoft-project/refs/heads/main/json-ld/microsoft-project-rest-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Microsoft Project Rest Api from Microsoft Project.
layout: jsonld
name: Microsoft Project Rest Api Context
namespaces:
- prefix: msproject
  uri: https://learn.microsoft.com/en-us/office/client-developer/project/schema/
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
  name: name
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: startDate
  type: dateTime
- container: ''
  name: finishDate
  type: dateTime
- container: ''
  name: createdDate
  type: dateTime
- container: ''
  name: modifiedDate
  type: dateTime
- container: ''
  name: isCheckedOut
  type: boolean
- container: ''
  name: checkedOutBy
  type: string
- container: ''
  name: percentComplete
  type: integer
- container: ''
  name: projectType
  type: integer
- container: ''
  name: projectSiteUrl
  type: reference
- container: ''
  name: start
  type: dateTime
- container: ''
  name: finish
  type: dateTime
- container: ''
  name: duration
  type: string
- container: ''
  name: isSummary
  type: boolean
- container: ''
  name: isMilestone
  type: boolean
- container: ''
  name: priority
  type: integer
- container: ''
  name: parentId
  type: string
- container: ''
  name: notes
  type: string
- container: ''
  name: isManuallyScheduled
  type: boolean
- container: ''
  name: work
  type: string
- container: ''
  name: remainingWork
  type: string
- container: ''
  name: actualWork
  type: string
- container: ''
  name: cost
  type: double
- container: ''
  name: email
  type: string
- container: ''
  name: resourceType
  type: integer
- container: ''
  name: isActive
  type: boolean
- container: ''
  name: isGeneric
  type: boolean
- container: ''
  name: maxUnits
  type: double
- container: ''
  name: standardRate
  type: double
- container: ''
  name: costCenter
  type: string
- container: ''
  name: group
  type: string
- container: ''
  name: baseCalendar
  type: string
- container: ''
  name: projectId
  type: string
- container: ''
  name: taskId
  type: string
- container: ''
  name: resourceId
  type: string
- container: ''
  name: resourceName
  type: string
- container: ''
  name: percentWorkComplete
  type: integer
- container: ''
  name: isStandardCalendar
  type: boolean
- container: ''
  name: fieldType
  type: integer
- container: ''
  name: entityType
  type: integer
- container: ''
  name: isRequired
  type: boolean
- container: ''
  name: status
  type: integer
- container: ''
  name: totalWork
  type: string
- container: ''
  name: totalActualWork
  type: string
- container: ''
  name: phaseId
  type: string
property_count: 47
provider_name: Microsoft Project
provider_slug: microsoft-project
slug: microsoft-project-rest-api-context
tags:
- Budgeting
- Gantt Charts
- Microsoft
- Portfolio Management
- Project Management
- Resource Management
- Scheduling
- Task Management
- JSON-LD
- Linked Data
- Semantic Web
---
