---
class_count: 9
classes:
- id
- type
- Member
- Department
- LeaveType
- Request
- Absence
- Workspace
- PublicHolidayCalendar
context_file: json-ld/absentify-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/absentify/refs/heads/main/json-ld/absentify-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Absentify from Absentify.
layout: jsonld
name: Absentify Context
namespaces:
- prefix: absentify
  uri: https://absentify.com/vocab#
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: name
  type: string
- container: ''
  name: email
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: member_id
  type: string
- container: ''
  name: department_id
  type: string
- container: ''
  name: leave_type_id
  type: string
- container: ''
  name: request_id
  type: string
- container: ''
  name: start
  type: date
- container: ''
  name: end
  type: date
- container: ''
  name: date
  type: date
- container: ''
  name: created_at
  type: dateTime
- container: ''
  name: updated_at
  type: dateTime
- container: ''
  name: color
  type: string
- container: ''
  name: approval_required
  type: boolean
- container: ''
  name: approved_by_id
  type: string
- container: ''
  name: approved_at
  type: dateTime
- container: ''
  name: workdays
  type: integer
- container: ''
  name: half_day
  type: boolean
- container: ''
  name: half_day_part
  type: string
- container: ''
  name: limit
  type: integer
- container: ''
  name: limit_type
  type: string
- container: ''
  name: active
  type: boolean
- container: ''
  name: reason
  type: string
- container: ''
  name: reason_required
  type: boolean
- container: ''
  name: country_code
  type: string
- container: ''
  name: year
  type: integer
- container: set
  name: holidays
  type: ''
- container: ''
  name: employment_start
  type: date
- container: ''
  name: employment_end
  type: date
- container: ''
  name: timezone
  type: string
- container: ''
  name: language
  type: string
- container: set
  name: manager_ids
  type: ''
- container: ''
  name: microsoft_365_id
  type: string
- container: ''
  name: plan
  type: string
- container: ''
  name: fiscal_year_start_month
  type: integer
property_count: 36
provider_name: Absentify
provider_slug: absentify
slug: absentify-context
tags:
- Absence Management
- HR
- Leave Management
- Microsoft Teams
- Human Resources
- JSON-LD
- Linked Data
- Semantic Web
---
