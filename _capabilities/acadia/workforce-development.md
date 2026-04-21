---
consumed_apis:
- acadia
description: Unified workforce development workflow using Acadia's Connected Worker Platform for managing employee training, skills matrices, work instructions, and quizzes. Used by HR managers, training coordinators, and operations managers to track and improve frontline worker capabilities.
layout: capability
name: Acadia Workforce Development
operations:
- description: List all digital work instructions
  method: GET
  name: list-work-instructions
  path: /v1/work-instructions
- description: List all employees with training completion data
  method: GET
  name: list-employees
  path: /v1/employees
- description: Get skills matrix for a specific employee
  method: GET
  name: get-employee-skills
  path: /v1/employees/{id}/skills
- description: List all job roles with training requirements
  method: GET
  name: list-roles
  path: /v1/roles
personas:
- description: HR professional managing employee training records, skills matrices, and role requirements
  id: hr-manager
  name: HR Manager
- description: Professional responsible for creating and assigning work instructions and quizzes
  id: training-coordinator
  name: Training Coordinator
- description: Manager monitoring team skill gaps, compliance, and training completion rates
  id: operations-manager
  name: Operations Manager
provider_name: Acadia
provider_slug: acadia
search_terms:
- acadia
- connected worker
- manufacturing
- workforce development
- list all active quizzes and assessments available in the platform
- knowledge management
- digital work instructions, employee skills, quizzes, and role management
- list all job roles with training requirements and completion rates
- list all digital work instructions
- professional responsible for creating and assigning work instructions and quizzes
- get employee skills matrix
- list all employees with training completion data
- list employees
- training
- end-to-end employee training management from work instructions to skill validation
- list job roles and training requirements
- hr professional managing employee training records, skills matrices, and role requirements
- list quizzes
- tracking and managing employee skills, roles, and career development
- list all job roles with training requirements
- training management
- operations manager
- list all digital work instructions with status and category filtering
- manager monitoring team skill gaps, compliance, and training completion rates
- create a new digital work instruction with title, category, and steps
- list work instructions
- manage digital work instructions
- get employee skills
- create work instruction
- list roles
- get skills matrix for a specific employee
- hr manager
- get the complete skills matrix for an employee showing required and completed skills
- list employees and their training status
- skills management
- list employees with training completion percentages, filtered by role or department
- training coordinator
slug: workforce-development
tags:
- Acadia
- Workforce Development
- Connected Worker
- Training Management
tools:
- description: List all digital work instructions with status and category filtering
  hints:
    openWorld: false
    readOnly: true
  name: list-work-instructions
- description: Create a new digital work instruction with title, category, and steps
  hints:
    openWorld: false
    readOnly: false
  name: create-work-instruction
- description: List employees with training completion percentages, filtered by role or department
  hints:
    openWorld: false
    readOnly: true
  name: list-employees
- description: Get the complete skills matrix for an employee showing required and completed skills
  hints:
    openWorld: false
    readOnly: true
  name: get-employee-skills
- description: List all active quizzes and assessments available in the platform
  hints:
    openWorld: false
    readOnly: true
  name: list-quizzes
- description: List all job roles with training requirements and completion rates
  hints:
    openWorld: false
    readOnly: true
  name: list-roles
---
