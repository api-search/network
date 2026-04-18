---
description: Represents an employee record from a connected HRIS integration in the Merge Unified API.
layout: schema
name: Employee
properties_list:
- description: The unique Merge-generated identifier.
  name: id
  type: string
- description: The third-party ID of this employee.
  name: remote_id
  type: string
- description: The employee's number in the organization.
  name: employee_number
  type: string
- description: The employee's first name.
  name: first_name
  type: string
- description: The employee's last name.
  name: last_name
  type: string
- description: The employee's full display name.
  name: display_full_name
  type: string
- description: The employee's work email address.
  name: work_email
  type: string
- description: The employee's personal email address.
  name: personal_email
  type: string
- description: The employee's mobile phone number.
  name: mobile_phone_number
  type: string
- description: The employee's date of birth.
  name: date_of_birth
  type: string
- description: The date the employee started working.
  name: start_date
  type: string
- description: The date the employee was terminated.
  name: termination_date
  type: string
- description: The current employment status.
  name: employment_status
  type: string
- description: The Merge ID of this employee's manager.
  name: manager
  type: string
- description: The Merge ID of the employee's company.
  name: company
  type: string
- description: The Merge ID of the employee's team.
  name: team
  type: string
- description: The Merge ID of the employee's pay group.
  name: pay_group
  type: string
- description: Groups this employee belongs to.
  name: groups
  type: array
- description: Whether the record was deleted in the third-party platform.
  name: remote_was_deleted
  type: boolean
- description: When the Merge record was created.
  name: created_at
  type: string
- description: When the Merge record was last modified.
  name: modified_at
  type: string
provider_name: Merge
provider_slug: merge
schema_file: json-schema/hris-api-employee-schema.json
slug: hris-api-employee
tags:
- Integrations
- Platform
- Unified API
title: Employee
---
