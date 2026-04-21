---
consumed_apis:
- absence-io
description: Unified workflow for managing employee absences, tracking leave balances, and administering organizational structure in Absence.io. Designed for HR managers, payroll teams, and integration developers building absence management workflows.
layout: capability
name: Absence.io Absence Management
operations:
- description: List all employee absences.
  method: GET
  name: list-absences
  path: /v1/absences
- description: Create a new absence record.
  method: POST
  name: create-absence
  path: /v1/absences
- description: Get an absence by ID.
  method: GET
  name: get-absence
  path: /v1/absences/{id}
- description: Update an absence.
  method: PUT
  name: update-absence
  path: /v1/absences/{id}
- description: Delete an absence.
  method: DELETE
  name: delete-absence
  path: /v1/absences/{id}
- description: List all employees.
  method: GET
  name: list-users
  path: /v1/employees
- description: Get an employee by ID.
  method: GET
  name: get-user
  path: /v1/employees/{id}
- description: List employee leave allowances.
  method: GET
  name: list-allowances
  path: /v1/allowances
- description: List departments.
  method: GET
  name: list-departments
  path: /v1/departments
- description: List locations.
  method: GET
  name: list-locations
  path: /v1/locations
- description: List absence reason types.
  method: GET
  name: list-reason-types
  path: /v1/absence-types
personas: []
provider_name: Absence.io
provider_slug: absence-io
search_terms:
- get detailed information about a specific employee.
- list employee absences. supports date range filtering and pagination.
- get an absence by id.
- list locations
- office locations.
- update an absence.
- list allowances
- organizational departments.
- list all organizational departments.
- employee absence records.
- create a new absence record for an employee.
- Payroll Processor
- list absences
- HR Manager
- delete an absence.
- list absence reason types.
- list employees
- employee absence tracking, approval workflows, and leave balance management
- list employee leave allowances.
- unified workflow for managing employee absences, leave balances, and org structure
- list leave allowances
- delete an absence record permanently.
- update an existing absence record (change dates, reason, etc.).
- delete absence
- leave management
- a specific employee record.
- absence management
- absences
- employee leave allowances.
- get an employee by id.
- absence reason types.
- list users
- list all employee absences.
- list all office locations.
- developers building integrations between absence.io and erp/hris systems
- list all absence reason types (vacation, sick leave, parental leave, etc.).
- list employee leave allowances and remaining balances for the year.
- list departments
- list locations.
- list all employees in the organization with their department and location assignments.
- update absence
- create a new absence record.
- get user
- list absence types
- get details of a specific absence record by its id.
- get employee
- Integration Developer
- hr professionals managing employee leave requests and approvals
- organizational structure including departments, locations, and employees
- payroll teams using absence data to calculate leave deductions and entitlements
- list all employees.
- payroll
- hr
- get absence
- employees
- create absence
- list reason types
- list departments.
- a specific absence record.
- employee records.
slug: absence-management
tags:
- Absence Management
- HR
- Leave Management
- Payroll
tools:
- description: List employee absences. Supports date range filtering and pagination.
  hints:
    openWorld: false
    readOnly: true
  name: list-absences
- description: Get details of a specific absence record by its ID.
  hints:
    openWorld: false
    readOnly: true
  name: get-absence
- description: Create a new absence record for an employee.
  hints:
    openWorld: false
    readOnly: false
  name: create-absence
- description: Update an existing absence record (change dates, reason, etc.).
  hints:
    idempotent: true
    openWorld: false
    readOnly: false
  name: update-absence
- description: Delete an absence record permanently.
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: delete-absence
- description: List all employees in the organization with their department and location assignments.
  hints:
    openWorld: false
    readOnly: true
  name: list-employees
- description: Get detailed information about a specific employee.
  hints:
    openWorld: false
    readOnly: true
  name: get-employee
- description: List employee leave allowances and remaining balances for the year.
  hints:
    openWorld: false
    readOnly: true
  name: list-leave-allowances
- description: List all organizational departments.
  hints:
    openWorld: false
    readOnly: true
  name: list-departments
- description: List all office locations.
  hints:
    openWorld: false
    readOnly: true
  name: list-locations
- description: List all absence reason types (vacation, sick leave, parental leave, etc.).
  hints:
    openWorld: false
    readOnly: true
  name: list-absence-types
---
