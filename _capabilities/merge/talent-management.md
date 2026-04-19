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
- hris list employees
- list all candidates.
- create employee
- create an employee in the hris.
- Recruiter
- end-to-end talent management combining hris and ats.
- list all employees.
- list all open job postings.
- list employees
- manages invoices, payments, and financial reporting.
- manages leads, opportunities, and crm activities.
- list all applications.
- manages candidate pipeline and hiring workflow.
- list time off requests.
- list all applications from the ats.
- create a new candidate.
- list all job postings.
- ats list jobs
- hris
- manages employee records, time off, and hr processes.
- list employees from the connected hris.
- candidate sourcing, applications, interviews, and offers.
- list applications
- ats list interviews
- employee management, benefits, time off, and payroll.
- time off management.
- job postings.
- create a new candidate in the ats.
- ats list applications
- HR Manager
- list all offers.
- list jobs
- manages tickets and customer support issues.
- invoicing, payments, expenses, and financial reporting.
- application tracking.
- list companies from the hris.
- file storage, sharing, and permissions.
- crm, leads, opportunities, and engagements.
- ats list offers
- hris create employee
- create a time off request.
- list time off
- talent management
- create candidate
- recruiting
- unified api
- platform
- hris list time off
- ats create candidate
- hris create time off
- hris list companies
- list scheduled interviews.
- ats
- merge
- candidate pipeline management.
- create a new employee.
- employee records.
- ats list candidates
- list candidates
- integrations
- ticket management and customer communication.
- list candidates from the connected ats.
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
