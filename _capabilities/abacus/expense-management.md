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
- finance
- list all members in the organization with pagination support
- suspend a member
- organization member management
- list members
- invite member
- list expense reports with filtering by status, member, or date range
- accounting
- HR Manager
- finance team member responsible for expense approvals and reimbursements
- get expense report details
- organization member provisioning, role management, and access control
- list all organization members
- individual member operations
- hr manager responsible for member provisioning and access management
- individual expense report
- member suspension
- get member details
- expense report management
- invite a new member to the organization
- get detailed information for a specific organization member
- get detailed information for a specific expense report including receipt url
- unified workflow for member management and expense tracking
- organization employee submitting expense reports for reimbursement
- abacus
- update a member's role, department, or status within the organization
- update member role or department
- list expense reports with filters
- expense management
- reimbursement
- update member
- Finance Administrator
- get member
- get expense
- members
- suspend member
- suspend an organization member to prevent expense submissions
- invite a new member to the organization with email and role assignment
- list expenses
- expense report submission, approval, and reimbursement workflows
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
