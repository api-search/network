---
consumed_apis:
- merge-hris
- merge-ats
description: Unified workflow combining HRIS and ATS APIs for end-to-end talent management, from candidate sourcing through onboarding and employee lifecycle. Used by HR teams, recruiters, and people operations.
layout: capability
name: Merge Talent Management
operations:
- description: List all candidates.
  method: GET
  name: list-candidates
  path: /v1/candidates
- description: Create a new candidate.
  method: POST
  name: create-candidate
  path: /v1/candidates
- description: List all applications.
  method: GET
  name: list-applications
  path: /v1/applications
- description: List all job postings.
  method: GET
  name: list-jobs
  path: /v1/jobs
- description: List all employees.
  method: GET
  name: list-employees
  path: /v1/employees
- description: Create a new employee.
  method: POST
  name: create-employee
  path: /v1/employees
- description: List time off requests.
  method: GET
  name: list-time-off
  path: /v1/time-off
personas: []
provider_name: Merge
provider_slug: merge
search_terms:
- ats create candidate
- talent management
- candidate pipeline management.
- list employees
- list all open job postings.
- list time off requests.
- hris create employee
- list employees from the connected hris.
- create candidate
- list all job postings.
- recruiting
- invoicing, payments, expenses, and financial reporting.
- list candidates
- list all offers.
- ats list offers
- end-to-end talent management combining hris and ats.
- list scheduled interviews.
- hris list time off
- hris create time off
- list all candidates.
- crm, leads, opportunities, and engagements.
- hris
- job postings.
- list jobs
- ats list candidates
- HR Manager
- manages employee records, time off, and hr processes.
- platform
- manages leads, opportunities, and crm activities.
- ats list applications
- create a new employee.
- manages invoices, payments, and financial reporting.
- create employee
- merge
- create a new candidate in the ats.
- unified api
- list all employees.
- employee records.
- application tracking.
- hris list employees
- list all applications.
- hris list companies
- ats list jobs
- file storage, sharing, and permissions.
- ats list interviews
- create a new candidate.
- ticket management and customer communication.
- manages candidate pipeline and hiring workflow.
- integrations
- employee management, benefits, time off, and payroll.
- create an employee in the hris.
- list candidates from the connected ats.
- list all applications from the ats.
- ats
- create a time off request.
- list time off
- manages tickets and customer support issues.
- list companies from the hris.
- candidate sourcing, applications, interviews, and offers.
- list applications
- time off management.
- Recruiter
slug: talent-management
tags:
- Merge
- Talent Management
- HRIS
- ATS
- Recruiting
tools:
- description: List candidates from the connected ATS.
  hints:
    readOnly: true
  name: ats-list-candidates
- description: Create a new candidate in the ATS.
  hints:
    readOnly: false
  name: ats-create-candidate
- description: List all applications from the ATS.
  hints:
    readOnly: true
  name: ats-list-applications
- description: List all open job postings.
  hints:
    readOnly: true
  name: ats-list-jobs
- description: List scheduled interviews.
  hints:
    readOnly: true
  name: ats-list-interviews
- description: List all offers.
  hints:
    readOnly: true
  name: ats-list-offers
- description: List employees from the connected HRIS.
  hints:
    readOnly: true
  name: hris-list-employees
- description: Create an employee in the HRIS.
  hints:
    readOnly: false
  name: hris-create-employee
- description: List companies from the HRIS.
  hints:
    readOnly: true
  name: hris-list-companies
- description: List time off requests.
  hints:
    readOnly: true
  name: hris-list-time-off
- description: Create a time off request.
  hints:
    readOnly: false
  name: hris-create-time-off
---
