---
api_count: 6
apis:
- description: Manage and interact with Tableau Server and Tableau Cloud resources programmatically including workbooks, data sources, users, and permissions.
  name: Tableau REST API
  slug: rest-api
- description: Build dashboard extensions that enable users to interact with data from other applications directly in Tableau dashboards.
  name: Tableau Extensions API
  slug: extensions-api
- description: Create, read, update, and delete data in .hyper files for use in Tableau Desktop and Server with high-performance data extract capabilities.
  name: Tableau Hyper API
  slug: hyper-api
- description: Embed Tableau visualizations into web applications using modern web components with v3 of the Embedding API.
  name: Tableau Embedding API
  slug: embedding-api
- description: Discover and query metadata about Tableau content using GraphQL, including workbooks, data sources, flows, and lineage information.
  name: Tableau Metadata API
  slug: metadata-api
- description: Python library that provides a convenient wrapper for the Tableau Server REST API for automation and integration workflows.
  name: Tableau Server Client (Python)
  slug: server-client-python
common:
- title: ''
  type: Portal
  url: https://www.tableau.com/developer
- title: ''
  type: Documentation
  url: https://www.tableau.com/developer/tools
- title: ''
  type: GettingStarted
  url: https://www.tableau.com/developer/getting-started
- title: ''
  type: Blog
  url: https://www.tableau.com/about/blog/developers
- title: ''
  type: Support
  url: https://www.tableau.com/support
- title: ''
  type: TermsOfService
  url: https://www.tableau.com/tos
- title: ''
  type: PrivacyPolicy
  url: https://www.tableau.com/privacy
- title: ''
  type: Training
  url: https://trailhead.salesforce.com/content/learn/modules/tableau-developer-platform/get-started-with-the-tableau-developer-platform
- title: ''
  type: GitHubOrganization
  url: https://github.com/tableau
created: '2024-01-01'
description: APIs and integration points for Tableau Desktop, a data visualization and business intelligence platform from Salesforce. Tableau provides REST APIs, embedding APIs, extension APIs, and SDK tools for building custom visualizations, automating server operations, and extending analytics capabilities.
features:
- description: Full CRUD operations on Tableau Server and Cloud resources including workbooks, data sources, and users.
  name: REST API Management
- description: Build custom interactive extensions that integrate third-party data and functionality into dashboards.
  name: Dashboard Extensions
- description: Create and manage .hyper data extract files with the Hyper API for optimized data loading.
  name: High-Performance Data Extracts
- description: Embed interactive Tableau visualizations in web applications with modern web components.
  name: Embedded Analytics
- description: Query content metadata and data lineage using GraphQL for governance and impact analysis.
  name: Metadata and Lineage
- description: Automate Tableau Server operations with the Python Server Client library.
  name: Python Automation
image: /assets/icons/tableau-desktop.png
integrations:
- description: Native integration with Salesforce CRM for embedded analytics and data connectivity.
  name: Salesforce
- description: High-performance data connectivity with Snowflake cloud data warehouse.
  name: Snowflake
- description: Cloud deployment on AWS with S3, Redshift, and Athena data source support.
  name: AWS
- description: Azure integration with Synapse Analytics, Blob Storage, and Azure Active Directory.
  name: Azure
- description: TabPy server for executing Python scripts in Tableau calculated fields.
  name: Python
- description: Collaboration integration for sharing and subscribing to Tableau content in Slack.
  name: Slack
layout: provider
modified: '2026-04-18'
name: Tableau Desktop
skills: []
slug: tableau-desktop
solutions: []
tags:
- Analytics
- Business Intelligence
- Data Visualization
- Desktop Application
url: https://raw.githubusercontent.com/api-evangelist/tableau-desktop/refs/heads/main/apis.yml
use_cases:
- description: Embed interactive dashboards and visualizations into customer-facing web applications.
  name: Embedded Analytics
- description: Automate data extract creation and refresh workflows using the Hyper API and REST API.
  name: Data Pipeline Automation
- description: Migrate workbooks and data sources between Tableau Server environments programmatically.
  name: Content Migration
- description: Build write-back forms, custom controls, and third-party integrations as dashboard extensions.
  name: Custom Dashboard Extensions
- description: Track data lineage and content dependencies using the Metadata API for impact analysis.
  name: Data Governance
---
