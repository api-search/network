---
consumed_apis:
- hcm
- recruiting
- approval-workflow
description: Unified workflow for HR administrators combining employee management, benefits, payroll, recruiting, talent management, and approval workflows across PeopleSoft HCM, Recruiting, and Approval Workflow Engine APIs.
layout: capability
name: PeopleSoft Human Resources
operations:
- description: Retrieve employee records with optional department and status filters.
  method: GET
  name: list-employees
  path: /v1/employees
- description: Retrieve details for a specific employee.
  method: GET
  name: get-employee
  path: /v1/employees/{employeeId}
- description: Retrieve benefit enrollment records.
  method: GET
  name: list-benefit-enrollments
  path: /v1/benefit-enrollments
- description: Retrieve payroll run history and status.
  method: GET
  name: list-payroll-runs
  path: /v1/payroll-runs
- description: Search available job postings.
  method: GET
  name: search-jobs
  path: /v1/jobs
- description: Retrieve details for a specific job posting.
  method: GET
  name: get-job-details
  path: /v1/jobs/{jobId}
- description: Submit a candidate application for a job posting.
  method: POST
  name: submit-application
  path: /v1/applications
- description: Retrieve pending HR approval requests.
  method: GET
  name: list-pending-approvals
  path: /v1/approvals
- description: Approve, deny, or push back an HR approval request.
  method: PUT
  name: process-approval
  path: /v1/approvals/{approvalId}
personas: []
provider_name: PeopleSoft
provider_slug: peoplesoft
search_terms:
- list employees
- process approval
- retrieve pending hr approval requests.
- peopletools platform services.
- individual approval operations
- submit application
- campus solutions.
- retrieve details for a specific employee.
- submit a candidate application for a job posting.
- approve, deny, or push back an hr approval request.
- search available job postings.
- erp
- list payroll runs
- list pending approvals
- job posting details
- payroll run history and status
- payroll
- benefit enrollment records
- retrieve payroll run history and status.
- crm
- campus solutions
- hcm
- list benefit enrollments
- human resources
- employee records
- candidate applications
- supply chain management
- get job details
- retrieve details for a specific job posting.
- hr approval requests
- human capital management.
- retrieve employee records with optional department and status filters.
- individual employee details
- talent management
- recruiting
- search jobs
- enterprise software
- peoplesoft
- retrieve benefit enrollment records.
- get employee
- financial management
- financial and supply chain management.
- job postings
slug: human-resources
tags:
- PeopleSoft
- Human Resources
- HCM
- Recruiting
- Talent Management
- Payroll
tools:
- description: Retrieve employee records with optional department and status filters.
  hints:
    openWorld: true
    readOnly: true
  name: list-employees
- description: Retrieve details for a specific employee.
  hints:
    openWorld: true
    readOnly: true
  name: get-employee
- description: Retrieve benefit enrollment records.
  hints:
    openWorld: true
    readOnly: true
  name: list-benefit-enrollments
- description: Retrieve payroll run history and status.
  hints:
    openWorld: true
    readOnly: true
  name: list-payroll-runs
- description: Search available job postings.
  hints:
    openWorld: true
    readOnly: true
  name: search-jobs
- description: Retrieve details for a specific job posting.
  hints:
    openWorld: true
    readOnly: true
  name: get-job-details
- description: Submit a candidate application for a job posting.
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: submit-application
- description: Retrieve pending HR approval requests.
  hints:
    openWorld: true
    readOnly: true
  name: list-pending-approvals
- description: Approve, deny, or push back an HR approval request.
  hints:
    destructive: false
    idempotent: true
    readOnly: false
  name: process-approval
---
