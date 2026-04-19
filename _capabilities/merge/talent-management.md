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
- list candidates from the connected ats.
- list all applications from the ats.
- file storage, sharing, and permissions.
- create a new candidate in the ats.
- list companies from the hris.
- Recruiter
- employee management, benefits, time off, and payroll.
- list jobs
- list candidates
- ats list candidates
- ats list jobs
- time off management.
- list all open job postings.
- invoicing, payments, expenses, and financial reporting.
- create an employee in the hris.
- crm, leads, opportunities, and engagements.
- create a new employee.
- ats create candidate
- application tracking.
- candidate pipeline management.
- manages invoices, payments, and financial reporting.
- hris list employees
- employee records.
- hris create employee
- create candidate
- hris list companies
- end-to-end talent management combining hris and ats.
- list all job postings.
- ats list interviews
- manages leads, opportunities, and crm activities.
- platform
- unified api
- manages employee records, time off, and hr processes.
- manages tickets and customer support issues.
- hris create time off
- create a new candidate.
- ats list offers
- candidate sourcing, applications, interviews, and offers.
- list all candidates.
- hris
- job postings.
- list all offers.
- HR Manager
- talent management
- list all applications.
- hris list time off
- list applications
- create employee
- list time off requests.
- ats list applications
- merge
- list all employees.
- list employees from the connected hris.
- ats
- list time off
- list employees
- manages candidate pipeline and hiring workflow.
- integrations
- recruiting
- ticket management and customer communication.
- list scheduled interviews.
- create a time off request.
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
