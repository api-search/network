---
api_count: 4
apis:
- description: REST API for accessing and managing Microsoft Project Online and Project Server data including projects, tasks, resources, assignments, calendars, custom fields, timesheets, lookup tables, and workflo
  name: Microsoft Project Online REST API
  slug: rest-api
- description: 'Client-Side Object Model API for programmatic access to Project Online and Project Server. Provides .NET, Silverlight, Windows Phone, and JavaScript interfaces for CRUD operations on projects, tasks, '
  name: Microsoft Project Online CSOM API
  slug: csom-api
- description: OData-based reporting feed for read-only access to Project Server and Project Online reporting data. Provides access to project, task, resource, assignment, and timesheet reporting tables and views vi
  name: Microsoft Project OData Reporting API
  slug: odata-reporting-api
- description: JavaScript API for building Office Add-ins that extend Microsoft Project desktop client. Enables reading task, resource, and view data from the active project within a task pane add-in.
  name: Microsoft Project JavaScript API
  slug: javascript-api
capabilities:
- description: 'Unified project management workflow combining the Microsoft Project Online REST API for managing projects, tasks, resources, assignments, timesheets, and workflows. Used by project managers, resource '
  name: Microsoft Project Management
  slug: project-management
common:
- title: ''
  type: Portal
  url: https://developer.microsoft.com/en-us/microsoft-365
- title: ''
  type: DeveloperPortal
  url: https://learn.microsoft.com/en-us/office/client-developer/project/project-programming-tasks
- title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/project-blog/bg-p/ProjectBlog
- title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/microsoft-365/project/compare-microsoft-project-management-software
- title: ''
  type: Support
  url: https://support.microsoft.com/
- title: ''
  type: GitHubRepository
  url: https://github.com/OfficeDev/Project-Samples
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/ms-project
- title: ''
  type: Training
  url: https://support.microsoft.com/en-us/project
- title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/office/client-developer/project/getting-started-developing-project-server-workflows
- title: ''
  type: GitHubOrganization
  url: https://github.com/OfficeDev
- title: Project Accelerator
  type: CodeExamples
  url: https://github.com/OfficeDev/Project-Accelerator
- title: Dataverse Plugin Sample
  type: CodeExamples
  url: https://github.com/OfficeDev/Project-Dataverse-Plugin-Sample
- title: ''
  type: SpectralRules
  url: rules/microsoft-project-spectral-rules.yml
- title: Project Management Workflow
  type: NaftikoCapability
  url: capabilities/project-management.yaml
- title: ''
  type: Vocabulary
  url: vocabulary/microsoft-project-vocabulary.yaml
created: '2024-01-15'
description: Microsoft Project is a project management software product developed by Microsoft. It provides tools for developing plans, assigning resources to tasks, tracking progress, managing budgets, and analyzing workloads. Microsoft Project offers REST APIs via SharePoint/Project Online, a Client-Side Object Model (CSOM), OData reporting feeds, and JavaScript APIs for building add-ins and integrations.
features:
- description: Visual timeline charts for project scheduling with task dependencies, critical path analysis, and milestone tracking.
  name: Gantt Charts
- description: Create, assign, and track tasks with predecessors, successors, constraints, and deadlines.
  name: Task Management
- description: Assign resources to tasks, view workloads, and manage resource availability and capacity.
  name: Resource Management
- description: Manage multiple projects as a portfolio with prioritization, budgeting, and resource allocation across projects.
  name: Portfolio Management
- description: Track project costs, budgets, and earned value metrics for financial project management.
  name: Budgeting and Cost Tracking
- description: Automatic scheduling with task dependencies, resource leveling, and critical path calculation.
  name: Scheduling Engine
- description: Time tracking and approval workflows for resource hours and project progress reporting.
  name: Timesheets
- description: Define enterprise custom fields, lookup tables, and formulas for extended project metadata.
  name: Custom Fields
- description: Pre-built and custom reports with Power BI integration for project, resource, and portfolio analytics.
  name: Reporting and Dashboards
- description: Demand management workflows for project proposals, approvals, and stage-gate governance.
  name: Workflow Automation
- description: SharePoint-based project sites with document libraries, issue tracking, and team communication.
  name: Collaboration
- description: Integration with Power BI, Power Automate, and Power Apps for extended project management scenarios.
  name: Power Platform Integration
image: /assets/icons/microsoft-project.png
integrations:
- description: View and manage project tasks directly within Microsoft Teams channels and tabs.
  name: Microsoft Teams
- description: Connect to Project Online data for interactive dashboards and portfolio analytics.
  name: Power BI
- description: SharePoint-based project sites for document management, collaboration, and task synchronization.
  name: SharePoint
- description: Deep integration with Outlook, Excel, Word, and other Microsoft 365 applications.
  name: Microsoft 365
- description: Automate project workflows, notifications, and approvals using Power Automate flows.
  name: Power Automate
- description: Build custom project management applications using Power Apps with Project data.
  name: Power Apps
- description: Connect project schedules with Azure DevOps work items for software development projects.
  name: Azure DevOps
- description: Integrate lightweight task planning in Planner with enterprise project management in Project.
  name: Microsoft Planner
- description: Project for the web stores data in Microsoft Dataverse, enabling custom integrations and extensions.
  name: Dataverse
- description: Export and import project data to Excel for custom analysis, reporting, and data manipulation.
  name: Excel
jsonld:
- class_count: 11
  name: Microsoft Project Rest Api Context
  property_count: 47
  slug: microsoft-project-rest-api-context
layout: provider
modified: '2026-04-18'
name: Microsoft Project
rules:
- name: Microsoft Project API Rules
  rule_count: 39
  severity_counts:
    error: 23
    hint: 0
    info: 7
    warn: 9
  slug: microsoft-project-spectral-rules
skills: []
slug: microsoft-project
solutions: []
tags:
- Budgeting
- Gantt Charts
- Microsoft
- Portfolio Management
- Project Management
- Resource Management
- Scheduling
- Task Management
url: https://raw.githubusercontent.com/api-evangelist/microsoft-project/refs/heads/main/apis.yml
use_cases:
- description: Plan and track IT infrastructure, software development, and digital transformation projects.
  name: IT Project Management
- description: Schedule construction phases, manage subcontractors, and track material costs.
  name: Construction Project Planning
- description: Coordinate product development timelines, milestones, and cross-functional team resources.
  name: Product Development
- description: Evaluate and prioritize project portfolios based on strategic alignment, ROI, and resource constraints.
  name: Portfolio Optimization
- description: Forecast resource demand, identify bottlenecks, and optimize resource allocation across projects.
  name: Resource Capacity Planning
- description: Manage interdependent projects as programs with shared resources and coordinated timelines.
  name: Program Management
- description: Track agile sprints, backlogs, and team velocity alongside traditional waterfall schedules.
  name: Agile Project Tracking
- description: Generate audit trails and compliance reports for project governance and regulatory requirements.
  name: Compliance Reporting
---
