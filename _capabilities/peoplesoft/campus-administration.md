---
consumed_apis:
- campus-solutions
- approval-workflow
description: Unified workflow for campus administrators combining student records, admissions, enrollment, financial aid, and approval workflows across PeopleSoft Campus Solutions and Approval Workflow Engine APIs.
layout: capability
name: PeopleSoft Campus Administration
operations:
- description: Retrieve student records.
  method: GET
  name: list-students
  path: /v1/students
- description: Retrieve details for a specific student.
  method: GET
  name: get-student
  path: /v1/students/{studentId}
- description: Retrieve admission applications.
  method: GET
  name: list-admission-applications
  path: /v1/admission-applications
- description: Retrieve class schedule and enrollment data.
  method: GET
  name: list-classes
  path: /v1/classes
- description: Retrieve financial aid award data.
  method: GET
  name: list-financial-aid-awards
  path: /v1/financial-aid-awards
- description: Retrieve pending campus approval requests.
  method: GET
  name: list-pending-approvals
  path: /v1/approvals
- description: Approve, deny, or push back a campus approval request.
  method: PUT
  name: process-approval
  path: /v1/approvals/{approvalId}
personas: []
provider_name: PeopleSoft
provider_slug: peoplesoft
search_terms:
- process approval
- peopletools platform services.
- individual student details
- individual approval operations
- class schedule and enrollment data
- student records
- campus solutions.
- campus approval requests
- retrieve admission applications.
- erp
- list pending approvals
- crm
- approve, deny, or push back a campus approval request.
- retrieve financial aid award data.
- financial aid
- retrieve pending campus approval requests.
- higher education
- financial aid awards
- campus solutions
- retrieve details for a specific student.
- hcm
- admission applications
- supply chain management
- human capital management.
- retrieve class schedule and enrollment data.
- list classes
- list students
- list financial aid awards
- enterprise software
- get student
- peoplesoft
- retrieve student records.
- admissions
- financial management
- financial and supply chain management.
- list admission applications
slug: campus-administration
tags:
- PeopleSoft
- Campus Solutions
- Higher Education
- Student Records
- Admissions
- Financial Aid
tools:
- description: Retrieve student records.
  hints:
    openWorld: true
    readOnly: true
  name: list-students
- description: Retrieve details for a specific student.
  hints:
    openWorld: true
    readOnly: true
  name: get-student
- description: Retrieve admission applications.
  hints:
    openWorld: true
    readOnly: true
  name: list-admission-applications
- description: Retrieve class schedule and enrollment data.
  hints:
    openWorld: true
    readOnly: true
  name: list-classes
- description: Retrieve financial aid award data.
  hints:
    openWorld: true
    readOnly: true
  name: list-financial-aid-awards
- description: Retrieve pending campus approval requests.
  hints:
    openWorld: true
    readOnly: true
  name: list-pending-approvals
- description: Approve, deny, or push back a campus approval request.
  hints:
    destructive: false
    idempotent: true
    readOnly: false
  name: process-approval
---
