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
- list employees
- ats list candidates
- employee records.
- manages candidate pipeline and hiring workflow.
- list all open job postings.
- hris list companies
- candidate pipeline management.
- list all applications.
- list applications
- HR Manager
- create candidate
- Recruiter
- list scheduled interviews.
- ticket management and customer communication.
- list all candidates.
- list jobs
- time off management.
- merge
- create a new candidate in the ats.
- create an employee in the hris.
- list all employees.
- create employee
- ats list offers
- list candidates
- hris create employee
- manages tickets and customer support issues.
- end-to-end talent management combining hris and ats.
- file storage, sharing, and permissions.
- list all offers.
- manages invoices, payments, and financial reporting.
- job postings.
- hris
- list all applications from the ats.
- ats create candidate
- candidate sourcing, applications, interviews, and offers.
- application tracking.
- ats
- list time off requests.
- ats list jobs
- ats list interviews
- list time off
- ats list applications
- list all job postings.
- manages employee records, time off, and hr processes.
- platform
- talent management
- recruiting
- manages leads, opportunities, and crm activities.
- unified api
- create a new candidate.
- employee management, benefits, time off, and payroll.
- crm, leads, opportunities, and engagements.
- hris create time off
- invoicing, payments, expenses, and financial reporting.
- create a new employee.
- hris list employees
- create a time off request.
- integrations
- hris list time off
- list candidates from the connected ats.
- list companies from the hris.
- list employees from the connected hris.
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
