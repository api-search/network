---
api_count: 13
apis:
- description: The Tableau REST API allows you to manage and change Tableau Server, Tableau Cloud site, and Tableau Prep Conductor resources programmatically, using HTTP.
  name: Tableau REST API
  slug: ''
- description: GraphQL-based API for querying metadata about Tableau content, data sources, and lineage information.
  name: Tableau Metadata API
  slug: ''
- description: API for creating, reading, and updating Hyper files, which are the data files that power Tableau extracts.
  name: Tableau Hyper API
  slug: ''
- description: JavaScript API for embedding Tableau visualizations in web applications with advanced interaction capabilities.
  name: Tableau Embedding API
  slug: ''
- description: Python library for programmatically updating Tableau workbook and data source files.
  name: Tableau Document API
  slug: ''
- description: Python library that wraps the Tableau REST API for easier programmatic access.
  name: Tableau Server Client (Python)
  slug: ''
- description: The Tableau Extensions API allows developers to create dashboard extensions and viz extensions that users can interact with directly in Tableau, enabling integration with other applications and custom
  name: Tableau Extensions API
  slug: ''
- description: The Tableau Web Data Connector (WDC) provides an SDK for building connectors to any data accessible over HTTP, allowing users to bring external data into Tableau for analysis and visualization.
  name: Tableau Web Data Connector
  slug: ''
- description: SDK for developing custom Tableau connectors using ODBC or JDBC drivers, including documentation, example files, a test harness, and a packaging tool for distribution.
  name: Tableau Connector SDK
  slug: ''
- description: The Analytics Extensions API allows integration of external analytics engines such as Python, R, MATLAB, and data science platforms with Tableau calculations for advanced analytics.
  name: Tableau Analytics Extensions API
  slug: ''
- description: Tableau Webhooks enable event-driven automation by sending HTTP POST notifications to specified URLs when events occur on Tableau Server or Tableau Cloud.
  name: Tableau Webhooks
  slug: ''
- description: The VizQL Data Service provides a programmatic HTTP interface to query published data sources outside of Tableau visualizations, enabling headless data access from any application.
  name: Tableau VizQL Data Service
  slug: ''
- description: The Tableau Pulse API enables programmatic creation, management, and querying of Tableau Pulse metrics and subscriptions, as well as embedding Pulse insights into web applications.
  name: Tableau Pulse API
  slug: ''
capabilities:
- description: Workflow for managing Tableau content including workbooks, data sources, views, sites, users, and permissions. Used by Tableau administrators and content managers.
  name: Tableau Content Management
  slug: content-management
common:
- title: ''
  type: DeveloperPortal
  url: https://www.tableau.com/developer
- title: ''
  type: Blog
  url: https://www.tableau.com/blog/developers
- title: ''
  type: Support
  url: https://www.tableau.com/support
- title: ''
  type: GitHubOrganization
  url: https://github.com/tableau
- title: ''
  type: StatusPage
  url: https://trust.tableau.com/
- title: ''
  type: ReleaseNotes
  url: https://help.tableau.com/current/tableau/en-us/whatsnew_all.htm
- title: ''
  type: TermsOfService
  url: https://www.tableau.com/legal
- title: ''
  type: PrivacyPolicy
  url: https://www.tableau.com/privacy
- title: ''
  type: SignUp
  url: https://www.tableau.com/products/trial
- title: ''
  type: Login
  url: https://www.tableau.com/tableau-login-hub
- title: ''
  type: Documentation
  url: https://help.tableau.com/
- title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/tableau
- title: ''
  type: YouTube
  url: https://www.youtube.com/@Tableau
- title: ''
  type: Training
  url: https://www.tableau.com/developer/learning
- title: ''
  type: SpectralRules
  url: rules/tableau-spectral-rules.yml
- title: Tableau REST API Shared Definition
  type: NaftikoCapability
  url: capabilities/shared/tableau-rest.yaml
- title: Content Management Workflow
  type: NaftikoCapability
  url: capabilities/content-management.yaml
created: '2024'
description: Tableau is a visual analytics platform transforming the way we use data to solve problems—empowering people and organizations to make the most of their data.
features:
- description: Publish, query, update, delete, and download data sources that define connections to data shared across workbooks.
  name: Data Source Management
- description: Publish, query, update, delete, and download workbooks containing views, dashboards, and stories.
  name: Workbook Management
- description: Create, configure, and manage Tableau Server and Cloud sites with full lifecycle control.
  name: Site Administration
- description: Add, update, and remove users and groups with role-based access control for content permissions.
  name: User and Group Management
- description: Query and set granular permissions on workbooks, data sources, projects, views, and flows.
  name: Permission Management
- description: Create and manage schedules for extract refreshes and subscriptions for automated content delivery.
  name: Schedule and Subscription Management
- description: Embed Tableau visualizations in web applications with interactive filtering and full API control.
  name: Embedded Analytics
- description: Query metadata about content, data sources, and data lineage using the GraphQL-based Metadata API.
  name: Metadata and Lineage
- description: Build custom connectors using ODBC or JDBC drivers to bring any data source into Tableau.
  name: Custom Connectors
- description: Enable event-driven automation with HTTP POST notifications when events occur on Tableau Server or Cloud.
  name: Webhooks
image: https://www.tableau.com/sites/default/files/tableau_logo_800.png
integrations:
- description: Native integration with Salesforce CRM for unified analytics across sales, service, and marketing data.
  name: Salesforce
- description: Share Tableau visualizations and receive metric alerts directly in Slack channels.
  name: Slack
- description: Extend Tableau calculations with Python and R scripts through the Analytics Extensions API.
  name: Python and R
- description: Optimized connector for Snowflake data warehouse with live query and extract support.
  name: Snowflake
- description: Connect to Google BigQuery for large-scale data analytics and visualization.
  name: Google BigQuery
jsonld:
- class_count: 0
  name: Tableau Context
  property_count: 14
  slug: tableau-context
- class_count: 0
  name: Tableau Rest Context
  property_count: 0
  slug: tableau-rest-context
layout: provider
modified: '2026-04-18'
name: Tableau
rules:
- name: Tableau API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: tableau-spectral-rules
skills: []
slug: tableau
solutions: []
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
url: https://www.tableau.com
use_cases:
- description: Automate the creation and distribution of business reports and dashboards across organizations.
  name: Enterprise Reporting
- description: Embed interactive visualizations and analytics directly into customer-facing applications.
  name: Embedded Analytics
- description: Track data lineage, manage permissions, and enforce data policies across the analytics platform.
  name: Data Governance
- description: Enable business users to explore data and create visualizations without IT involvement.
  name: Self-Service Analytics
- description: Programmatically migrate workbooks, data sources, and configurations between Tableau environments.
  name: Content Migration
---
