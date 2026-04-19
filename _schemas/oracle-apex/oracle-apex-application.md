---
description: Schema for an Oracle Application Express (APEX) application definition including its pages, regions, items, buttons, processes, computations, and shared components. Based on the APEX application model as documented in the Oracle APEX Application Builder and Blueprint specification.
layout: schema
name: Oracle APEX Application
properties_list:
- description: Unique numeric identifier for the APEX application within the workspace
  name: application_id
  type: integer
- description: Display name of the APEX application
  name: application_name
  type: string
- description: Logical group to which the application belongs for organizational purposes
  name: application_group
  type: string
- description: Name of the APEX workspace that owns this application
  name: workspace
  type: string
- description: Numeric identifier of the APEX workspace
  name: workspace_id
  type: integer
- description: Database schema (parsing schema) used by the application for SQL and PL/SQL execution
  name: schema
  type: string
- description: Short alphanumeric alias for the application, used in friendly URLs
  name: alias
  type: string
- description: Application version string
  name: version
  type: string
- description: Current availability status of the application
  name: application_status
  type: string
- description: Controls whether the application can be modified in the Application Builder
  name: build_status
  type: string
- description: Default Oracle date format mask for the application
  name: date_format
  type: string
- description: Default Oracle timestamp format mask for the application
  name: timestamp_format
  type: string
- description: Default Oracle timestamp with time zone format mask
  name: timestamp_tz_format
  type: string
- description: Primary language of the application (IANA language tag)
  name: language
  type: string
- description: APEX version compatibility mode for the application
  name: compatibility_mode
  type: string
- description: ''
  name: authentication
  type: object
- description: Name of the authorization scheme controlling access to the entire application
  name: authorization_scheme
  type: string
- description: ''
  name: session_management
  type: object
- description: ''
  name: navigation
  type: object
- description: ''
  name: user_interface
  type: object
- description: Collection of pages that comprise the application
  name: pages
  type: array
- description: ''
  name: shared_components
  type: object
- description: REST data source definitions for external API integration
  name: rest_data_sources
  type: array
- description: Web credential stores for authenticating REST data source requests
  name: web_credentials
  type: array
- description: Timestamp when the application was created
  name: created_on
  type: string
- description: Timestamp when the application was last modified
  name: last_updated_on
  type: string
- description: Username of the developer who last modified the application
  name: last_updated_by
  type: string
provider_name: Oracle APEX
provider_slug: oracle-apex
schema_file: json-schema/oracle-apex-application-schema.json
slug: oracle-apex-application
tags:
- APEX
- Cloud
- Database
- Development Platform
- Enterprise
- Generative AI
- Low-Code
- Oracle
- ORDS
- PL/SQL
- REST API
- Web Applications
- Workflow
title: Oracle APEX Application
---
