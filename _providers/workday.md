---
api_count: 20
apis:
- description: Human Capital Management API for managing workforce data, recruiting, talent management, and payroll. Provides RESTful endpoints for core HR operations.
  name: Workday HCM API
  slug: hcm-api
- description: Financial Management API for accounting, procurement, expenses, and financial reporting. Enables programmatic access to financial data and workflows.
  name: Workday Financial Management API
  slug: financial-management-api
- description: Recruiting API for managing job postings, candidates, applications, and hiring workflows. Supports interview feedback and prospect management.
  name: Workday Recruiting API
  slug: recruiting-api
- description: Time Tracking API for managing employee time entry, timesheets, time clock events, and time validations.
  name: Workday Time Tracking API
  slug: time-tracking-api
- description: Benefits API for managing employee benefits, enrollments, and coverage. Provides endpoints for benefits administration workflows.
  name: Workday Benefits API
  slug: benefits-api
- description: Absence Management API for managing leave balances, time-off requests, leaves of absence, and eligible absence types for workers.
  name: Workday Absence Management API
  slug: absence-management-api
- description: Compensation API for managing employee compensation plans, scorecards, scorecard results, and one-time payment requests.
  name: Workday Compensation API
  slug: compensation-api
- description: Payroll API for managing pay groups, pay group details, tax rates, payroll inputs, and pay components.
  name: Workday Payroll API
  slug: payroll-api
- description: Person API for managing worker person data including personal information, contact details, and organizational relationships.
  name: Workday Person API
  slug: person-api
- description: Performance Management API for managing performance reviews, feedback badges, goals, and employee performance evaluations.
  name: Workday Performance Management API
  slug: performance-management-api
- description: Talent Management API for managing mentorships, talent profiles, career development, and succession planning.
  name: Workday Talent Management API
  slug: talent-management-api
- description: Common API providing shared reference data, lookup values, and utility endpoints used across other Workday REST API services.
  name: Workday Common API
  slug: common-api
- description: Staffing API for managing organizational assignments, job profiles, positions, supervisory organizations, and worker staffing events.
  name: Workday Staffing API
  slug: staffing-api
- description: Strategic Sourcing API for managing sourcing events, awards, contracts, suppliers, spend categories, and procurement workflows.
  name: Workday Strategic Sourcing API
  slug: strategic-sourcing-api
- description: Standards-based SOAP API providing programmatic access to Workday business management services with WSDL and XML Schema definitions. Covers 55 service areas including Human Resources, Payroll, Benefit
  name: Workday SOAP Web Services API
  slug: soap-web-services-api
- description: Prism Analytics REST API for working with Workday Prism Analytics tables, data change tasks, and datasets. Enables programmatic creation and management of analytics data.
  name: Workday Prism Analytics API
  slug: prism-analytics-api
- description: Workday Extend platform for building custom applications that integrate with Workday. Provides low-code and no-code developer tools for creating business solutions.
  name: Workday Extend API
  slug: extend-api
- description: Report-as-a-Service (RaaS) exposes custom reports as RESTful web services, enabling programmatic access to report data. Supports query parameters for filtering and returns data in multiple formats.
  name: Workday Report-as-a-Service API
  slug: raas-api
- description: Adaptive Planning REST and XML APIs for managing planning data, accounts, dimensions, and custom reports. Supports integration with enterprise planning and budgeting workflows.
  name: Workday Adaptive Planning API
  slug: adaptive-planning-api
- description: Workday Query Language (WQL) API enabling SQL-like querying of Workday data through REST endpoints. Provides high-performance data access controlled via OAuth 2.0 tokens.
  name: Workday WQL API
  slug: wql-api
capabilities:
- description: Unified analytics and reporting combining Prism Analytics, WQL, and Report-as-a-Service APIs for business analysts to query data, manage datasets, and access custom reports.
  name: Workday Analytics and Reporting
  slug: analytics-and-reporting
- description: Unified compensation and payroll management combining Compensation, Payroll, and Benefits APIs for payroll administrators to manage pay plans, benefits enrollment, and payroll processing.
  name: Workday Compensation and Payroll
  slug: compensation-and-payroll
- description: Unified financial operations combining Financial Management and procurement data for finance teams to manage accounting, suppliers, expenses, and invoices.
  name: Workday Finance and Procurement
  slug: finance-and-procurement
- description: Unified talent and performance management combining Recruiting, Talent, and Performance Management APIs for HR and talent leads to manage hiring pipelines, career development, and performance evaluati
  name: Workday Talent and Performance
  slug: talent-and-performance
- description: Unified time and absence management combining Time Tracking and Absence Management APIs for HR operations to manage timesheets, time-off requests, and leave balances.
  name: Workday Time and Absence
  slug: time-and-absence
- description: Unified workforce management combining HCM, Person, Staffing, and Common APIs for HR administrators to manage workers, organizations, positions, and reference data.
  name: Workday Workforce Management
  slug: workforce-management
common:
- title: ''
  type: GettingStarted
  url: https://community.workday.com/api-start
- title: ''
  type: Authentication
  url: https://community.workday.com/sites/default/files/file-hosting/restapi/index.html#authentication
- title: ''
  type: RateLimits
  url: https://community.workday.com/articles/16827
- title: ''
  type: StatusPage
  url: https://community.workday.com/trust/status
- title: ''
  type: TermsOfService
  url: https://www.workday.com/en-us/legal.html
- title: ''
  type: PrivacyPolicy
  url: https://www.workday.com/en-us/privacy.html
- title: ''
  type: Documentation
  url: https://community.workday.com/api
- title: ''
  type: Console
  url: https://developer.workday.com/about
- title: ''
  type: Blog
  url: https://blog.workday.com/en-us/application-development.html
- title: ''
  type: GitHubOrganization
  url: https://github.com/workday
- title: ''
  type: SignUp
  url: https://resourcecenter.workday.com/
- title: ''
  type: Support
  url: https://www.workday.com/en-us/services/support.html
- title: ''
  type: Marketplace
  url: https://marketplace.workday.com/en-US/home
- title: ''
  type: Partners
  url: https://www.workday.com/en-us/company/partners/overview.html
- title: ''
  type: APIReference
  url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
- title: ''
  type: JSONLD
  url: json-ld/context.jsonld
- title: ''
  type: SpectralRules
  url: rules/workday-spectral-rules.yml
- title: ''
  type: Vocabulary
  url: vocabulary/workday-vocabulary.yaml
created: '2024-01-15'
description: Collection of Workday REST and SOAP APIs for human capital management, financial management, enterprise planning, analytics, and platform extensibility.
features:
- description: Comprehensive HCM suite for managing the entire employee lifecycle from hiring to retirement with global compliance.
  name: Human Capital Management
- description: Cloud-native financial management with real-time accounting, procurement, expenses, and revenue management.
  name: Financial Management
- description: Enterprise planning and budgeting with collaborative forecasting, scenario modeling, and rolling forecasts.
  name: Adaptive Planning
- description: Augmented analytics platform combining Workday and third-party data for actionable business intelligence.
  name: Prism Analytics
- description: End-to-end recruiting solution with job requisitions, candidate management, and interview scheduling.
  name: Recruiting
- description: Skills-based talent optimization with performance reviews, succession planning, and career development.
  name: Talent Management
- description: Global payroll processing with automated calculations, tax compliance, and pay slip generation.
  name: Payroll
- description: Automated time entry, timesheet management, leave balances, and absence request workflows.
  name: Time and Absence Tracking
- description: Low-code platform for building custom applications that integrate natively with the Workday ecosystem.
  name: Workday Extend
- description: Expose custom Workday reports as RESTful web services for programmatic data access and integration.
  name: Report-as-a-Service
image: /assets/icons/workday.png
integrations:
- description: Sync workforce and customer data between Workday HCM and Salesforce CRM for unified employee and customer insights.
  name: Salesforce
- description: Integrate Workday with Microsoft Teams, Outlook, and Azure AD for single sign-on and productivity workflows.
  name: Microsoft 365
- description: Connect Workday HR processes with ServiceNow ITSM for automated employee service delivery and ticket management.
  name: ServiceNow
- description: Enable Workday notifications, approvals, and time-off requests directly within Slack channels and DMs.
  name: Slack
- description: Integrate Workday payroll with ADP for third-party payroll processing and tax filing services.
  name: ADP
- description: Connect Workday financial management with SAP ERP for cross-system accounting and procurement workflows.
  name: SAP
- description: Integrate Workday with Greenhouse recruiting for seamless candidate pipeline management and hiring workflows.
  name: Greenhouse
- description: Connect Workday with Okta for identity management, single sign-on, and automated user provisioning.
  name: Okta
jsonld:
- class_count: 0
  name: Absencemanagement Context
  property_count: 0
  slug: absenceManagement-context
- class_count: 0
  name: Benefits Context
  property_count: 0
  slug: benefits-context
- class_count: 0
  name: Common Context
  property_count: 0
  slug: common-context
- class_count: 0
  name: Compensation Context
  property_count: 0
  slug: compensation-context
- class_count: 3
  name: context Context
  property_count: 19
  slug: context
- class_count: 0
  name: Financialmanagement Context
  property_count: 0
  slug: financialManagement-context
- class_count: 0
  name: Hcm Context
  property_count: 0
  slug: hcm-context
- class_count: 0
  name: Payroll Context
  property_count: 0
  slug: payroll-context
- class_count: 0
  name: Performancemanagement Context
  property_count: 0
  slug: performanceManagement-context
- class_count: 0
  name: Person Context
  property_count: 0
  slug: person-context
- class_count: 0
  name: Prismanalytics Context
  property_count: 0
  slug: prismAnalytics-context
- class_count: 0
  name: Raas Context
  property_count: 0
  slug: raas-context
- class_count: 0
  name: Recruiting Context
  property_count: 0
  slug: recruiting-context
- class_count: 0
  name: Staffing Context
  property_count: 0
  slug: staffing-context
- class_count: 0
  name: Talent Context
  property_count: 0
  slug: talent-context
- class_count: 0
  name: Timetracking Context
  property_count: 0
  slug: timeTracking-context
- class_count: 0
  name: Wql Context
  property_count: 0
  slug: wql-context
layout: provider
modified: '2026-04-18'
name: Workday
rules:
- name: Workday API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: workday-spectral-rules
skills: []
slug: workday
solutions: []
tags:
- Cloud Computing
- Enterprise Software
- Financial Management
- HCM
- SaaS
url: https://raw.githubusercontent.com/api-evangelist/workday/refs/heads/main/apis.yml
use_cases:
- description: Automate new hire onboarding workflows including position assignment, benefits enrollment, and system provisioning.
  name: Employee Onboarding
- description: Model headcount scenarios, track open positions, and align workforce supply with business demand.
  name: Workforce Planning
- description: Streamline employee expense reporting with automated policy enforcement, approval workflows, and reimbursement.
  name: Expense Management
- description: Generate regulatory compliance reports for labor laws, tax requirements, and industry-specific mandates.
  name: Compliance Reporting
- description: Conduct structured performance evaluations with goal tracking, feedback collection, and calibration.
  name: Performance Reviews
- description: Integrate payroll data with third-party systems for tax filing, benefits administration, and general ledger posting.
  name: Payroll Integration
---
