---
description: Request body for the login endpoint.
layout: schema
name: LoginRequest
properties_list:
- description: The resource type identifier. Must be set to "login".
  name: '@type'
  type: string
- description: The Informatica Intelligent Cloud Services username.
  name: username
  type: string
- description: The account password.
  name: password
  type: string
provider_name: Informatica
provider_slug: informatica
schema_file: json-schema/informatica-platform-rest-login-request-schema.json
slug: informatica-platform-rest-login-request
tags:
- Address Verification
- B2B Gateway
- Cloud Services
- Data Governance
- Data Integration
- Data Profiling
- Data Quality
- Enterprise Software
- ETL
- IDMC
- IICS
- Master Data Management
- Reference Data Management
title: LoginRequest
---
