---
description: Successful login response containing the session ID and server URL for subsequent API calls.
layout: schema
name: LoginResponse
properties_list:
- description: The user ID.
  name: id
  type: string
- description: The organization ID.
  name: orgId
  type: string
- description: The organization UUID.
  name: orgUuid
  type: string
- description: The username used to log in.
  name: name
  type: string
- description: The first name of the user.
  name: firstName
  type: string
- description: The last name of the user.
  name: lastName
  type: string
- description: The job title of the user.
  name: title
  type: string
- description: The phone number of the user.
  name: phone
  type: string
- description: The email address of the user.
  name: emails
  type: string
- description: The time zone of the user (e.g., America/Los_Angeles).
  name: timezone
  type: string
- description: The base URL to use in version 2 REST API calls. Use this URL as the base for all subsequent v2 API requests.
  name: serverUrl
  type: string
- description: The REST API session ID. Include this value in the icSessionId header for all subsequent requests. Expires after 30 minutes of inactivity.
  name: icSessionId
  type: string
- description: The security question for the user account.
  name: securityQuestion
  type: string
- description: The security answer (returned as empty string).
  name: securityAnswer
  type: string
- description: The time the user account was created.
  name: createTime
  type: string
- description: The time the user account was last updated.
  name: updateTime
  type: string
provider_name: Informatica
provider_slug: informatica
schema_file: json-schema/informatica-platform-rest-login-response-schema.json
slug: informatica-platform-rest-login-response
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
title: LoginResponse
---
