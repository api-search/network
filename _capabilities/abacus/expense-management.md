---
consumed_apis:
- abacus-api
description: Unified workflow for managing employee expenses, reimbursements, and member provisioning. Enables finance teams and administrators to automate expense reporting, track spending by member or category, and manage organizational membership.
layout: capability
name: Abacus Expense Management
operations:
- description: List all organization members
  method: GET
  name: list-members
  path: /v1/members
- description: Invite a new member to the organization
  method: POST
  name: invite-member
  path: /v1/members
- description: Get member details
  method: GET
  name: get-member
  path: /v1/members/{member_id}
- description: Update member role or department
  method: PUT
  name: update-member
  path: /v1/members/{member_id}
- description: Suspend a member
  method: POST
  name: suspend-member
  path: /v1/members/{member_id}/suspend
- description: List expense reports with filters
  method: GET
  name: list-expenses
  path: /v1/expenses
- description: Get expense report details
  method: GET
  name: get-expense
  path: /v1/expenses/{expense_id}
personas: []
provider_name: Abacus
provider_slug: abacus
search_terms:
- update member
- get member
- organization member management
- list expense reports with filtering by status, member, or date range
- members
- get expense report details
- accounting
- suspend an organization member to prevent expense submissions
- list all members in the organization with pagination support
- expense report management
- unified workflow for member management and expense tracking
- invite member
- get expense
- individual expense report
- hr manager responsible for member provisioning and access management
- invite a new member to the organization
- update a member's role, department, or status within the organization
- get detailed information for a specific expense report including receipt url
- expense report submission, approval, and reimbursement workflows
- HR Manager
- suspend member
- list expenses
- list expense reports with filters
- expense management
- finance team member responsible for expense approvals and reimbursements
- individual member operations
- suspend a member
- finance
- Finance Administrator
- invite a new member to the organization with email and role assignment
- list all organization members
- organization member provisioning, role management, and access control
- get member details
- update member role or department
- reimbursement
- list members
- get detailed information for a specific organization member
- abacus
- organization employee submitting expense reports for reimbursement
- member suspension
slug: expense-management
tags:
- Abacus
- Expense Management
- Finance
- Reimbursement
- Members
tools:
- description: List all members in the organization with pagination support
  hints:
    openWorld: false
    readOnly: true
  name: list-members
- description: Invite a new member to the organization with email and role assignment
  hints:
    destructive: false
    idempotent: false
    readOnly: false
  name: invite-member
- description: Get detailed information for a specific organization member
  hints:
    openWorld: false
    readOnly: true
  name: get-member
- description: Update a member's role, department, or status within the organization
  hints:
    destructive: false
    idempotent: true
    readOnly: false
  name: update-member
- description: Suspend an organization member to prevent expense submissions
  hints:
    destructive: true
    idempotent: true
    readOnly: false
  name: suspend-member
- description: List expense reports with filtering by status, member, or date range
  hints:
    openWorld: false
    readOnly: true
  name: list-expenses
- description: Get detailed information for a specific expense report including receipt URL
  hints:
    openWorld: false
    readOnly: true
  name: get-expense
---
