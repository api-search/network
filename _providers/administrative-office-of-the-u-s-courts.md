---
api_count: 2
apis:
- description: The PACER Authentication API allows users to authenticate automatically and without a user interface, facilitating programmatic access for automated systems to court records. Users provide PACER crede
  name: PACER Authentication API
  slug: pacer-authentication-api
- description: The PACER Case Locator (PCL) API is a REST API providing programmatic access to a nationwide index of federal court cases across all Federal Appellate, District, and Bankruptcy courts. Supports both i
  name: PACER Case Locator (PCL) API
  slug: pacer-case-locator-pcl-api
common:
- title: ''
  type: Website
  url: https://www.uscourts.gov/
- title: ''
  type: Portal
  url: https://pacer.uscourts.gov/
- title: ''
  type: DeveloperPortal
  url: https://pacer.uscourts.gov/file-case/developer-resources
- title: ''
  type: SignUp
  url: https://pacer.uscourts.gov/register-account
- title: ''
  type: Contact
  url: https://pacer.uscourts.gov/contact-us
created: '2024-11-20'
description: The Administrative Office of the United States Courts is the administrative agency of the United States federal court system, established in 1939. It provides legislative, administrative, legal, financial, management, program, and information technology support services to the federal courts. The agency operates PACER (Public Access to Court Electronic Records), which provides programmatic access to case and docket information from Federal Appellate, District, and Bankruptcy courts via the PACER Authentication API and PACER Case Locator (PCL) REST API. The agency also provides CM/ECF developer resources for building tools that interface with the Case Management and Electronic Case Filing system.
features:
- description: Programmatic search across a nationwide index of all Federal Appellate, District, and Bankruptcy court cases using the PCL REST API, supporting case search and party search with immediate and batch result modes.
  name: Federal Court Case Search
- description: Token-based authentication API enabling automated systems to obtain PACER authentication tokens without requiring a user interface, suitable for integration into automated data pipelines and legal research tools.
  name: Automated PACER Authentication
- description: Technical resources for developers building tools that interface with the Case Management and Electronic Case Filing (CM/ECF) system, including XML tag specifications, NextGen CM/ECF documentation, and release notes for appellate and bankruptcy systems.
  name: CM/ECF Developer Integration
- description: JSON and XML data feeds providing court lookup information for identifying CM/ECF courts and their configurations, available for integration into court filing software.
  name: Court Lookup Data Feeds
- description: Specialized resources for bankruptcy petition preparation software and case trustee management software vendors, including creditor claim filing specifications and official form changes.
  name: Bankruptcy Filing Integration
- description: Commercial users can run large batch data pulls via the PCL API, with recommended off-peak hours (6 p.m. to 6 a.m. Central Time) to minimize system impact.
  name: Bulk Data Access
image: /assets/icons/administrative-office-of-the-u-s-courts.png
integrations:
- description: Case Management and Electronic Case Filing system for all federal courts.
  name: CM/ECF System
- description: Nationwide index of federal court cases searchable via REST API.
  name: PACER Case Locator
- description: Next-generation electronic filing system with enhanced developer integration support.
  name: NextGen CM/ECF
layout: provider
modified: '2026-04-19'
name: Administrative Office of the U.S. Courts
skills: []
slug: administrative-office-of-the-u-s-courts
solutions: []
tags:
- Courts
- Federal Government
- Legal
- PACER
- Case Records
- Judiciary
- Open Data
url: https://raw.githubusercontent.com/api-evangelist/administrative-office-of-the-u-s-courts/refs/heads/main/apis.yml
use_cases:
- description: Law firms and legal research platforms can use the PCL API to programmatically search federal court case indexes and retrieve case and party information for automated legal research workflows.
  name: Legal Research Automation
- description: Corporate legal departments can monitor federal court filings involving specific parties, cases, or subject matters using automated PCL API queries.
  name: Litigation Monitoring
- description: Bankruptcy petition preparation software and trustee management applications can integrate with CM/ECF and PACER APIs to file documents, retrieve case data, and manage creditor information.
  name: Bankruptcy Software Integration
- description: Academic researchers and legal analytics firms can build datasets of federal court case activity using batch PCL API searches across federal court jurisdictions.
  name: Court Data Analytics
- description: Legal technology companies can build PACER-integrated products for case tracking, docket monitoring, and court record retrieval using the PACER Authentication and PCL APIs.
  name: Legal Technology Development
---
