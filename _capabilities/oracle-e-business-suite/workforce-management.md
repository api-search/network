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
- e-business suite
- employee management.
- get employee by id.
- human resources
- oracle
- retrieve organizations.
- payroll management.
- business applications
- erp
- retrieve employees.
- get positions
- get organizations
- retrieve benefit enrollments.
- retrieve assignments.
- update employee record.
- get employees
- get benefit enrollments
- retrieve payroll runs.
- retrieve payroll definitions.
- get payrolls
- list payrolls.
- create employee
- get employee by id
- enterprise
- payroll
- update employee
- organization management.
- workforce management
- create an employee record.
- list organizations.
- retrieve positions.
- list employees.
- get assignments
- get payroll runs
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
