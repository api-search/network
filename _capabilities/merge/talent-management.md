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
- hris create employee
- ats list applications
- crm, leads, opportunities, and engagements.
- integrations
- unified api
- list candidates
- invoicing, payments, expenses, and financial reporting.
- create a new employee.
- manages tickets and customer support issues.
- list jobs
- employee management, benefits, time off, and payroll.
- candidate sourcing, applications, interviews, and offers.
- Recruiter
- job postings.
- create candidate
- list time off requests.
- list all offers.
- hris create time off
- list time off
- end-to-end talent management combining hris and ats.
- HR Manager
- list all job postings.
- hris
- list applications
- list candidates from the connected ats.
- list employees from the connected hris.
- list all applications from the ats.
- create a new candidate.
- ats
- application tracking.
- talent management
- ats list jobs
- create a new candidate in the ats.
- list employees
- create employee
- manages leads, opportunities, and crm activities.
- platform
- recruiting
- merge
- manages employee records, time off, and hr processes.
- list all open job postings.
- hris list companies
- manages invoices, payments, and financial reporting.
- employee records.
- list companies from the hris.
- candidate pipeline management.
- ats list interviews
- ats list candidates
- hris list time off
- create a time off request.
- list scheduled interviews.
- file storage, sharing, and permissions.
- create an employee in the hris.
- hris list employees
- list all applications.
- ticket management and customer communication.
- list all candidates.
- manages candidate pipeline and hiring workflow.
- ats create candidate
- ats list offers
- time off management.
- list all employees.
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
