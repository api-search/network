---
consumed_apis:
- oracle-human-resources
description: Human capital management combining HR, payroll, benefits, and organizational management. Used by HR administrators and payroll managers for employee lifecycle operations.
layout: capability
name: Oracle EBS Workforce Management
operations:
- description: List employees.
  method: GET
  name: get-employees
  path: /v1/employees
- description: List organizations.
  method: GET
  name: get-organizations
  path: /v1/organizations
- description: List payrolls.
  method: GET
  name: get-payrolls
  path: /v1/payrolls
personas: []
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
search_terms:
- retrieve payroll definitions.
- create employee
- get employee by id.
- get employee by id
- get assignments
- get payrolls
- update employee record.
- retrieve organizations.
- get payroll runs
- retrieve benefit enrollments.
- business applications
- e-business suite
- list organizations.
- list payrolls.
- oracle
- retrieve positions.
- enterprise
- retrieve employees.
- erp
- get employees
- retrieve assignments.
- get benefit enrollments
- workforce management
- list employees.
- create an employee record.
- payroll
- human resources
- payroll management.
- employee management.
- get organizations
- get positions
- retrieve payroll runs.
- update employee
- organization management.
slug: workforce-management
tags:
- Oracle
- Human Resources
- Workforce Management
- Payroll
tools:
- description: Retrieve employees.
  hints:
    openWorld: true
    readOnly: true
  name: get-employees
- description: Create an employee record.
  hints:
    readOnly: false
  name: create-employee
- description: Get employee by ID.
  hints:
    readOnly: true
  name: get-employee-by-id
- description: Update employee record.
  hints:
    idempotent: true
    readOnly: false
  name: update-employee
- description: Retrieve assignments.
  hints:
    readOnly: true
  name: get-assignments
- description: Retrieve organizations.
  hints:
    readOnly: true
  name: get-organizations
- description: Retrieve positions.
  hints:
    readOnly: true
  name: get-positions
- description: Retrieve payroll definitions.
  hints:
    readOnly: true
  name: get-payrolls
- description: Retrieve payroll runs.
  hints:
    readOnly: true
  name: get-payroll-runs
- description: Retrieve benefit enrollments.
  hints:
    readOnly: true
  name: get-benefit-enrollments
---
