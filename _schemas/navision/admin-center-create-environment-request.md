---
description: ''
layout: schema
name: CreateEnvironmentRequest
properties_list:
- description: Type of environment to create
  name: environmentType
  type: string
- description: Country to create the environment within
  name: countryCode
  type: string
- description: Logical ring group (only Sandbox may be created in Preview ring)
  name: ringName
  type: string
- description: Application version (e.g., 26.0.0.0)
  name: applicationVersion
  type: string
provider_name: Microsoft Dynamics NAV
provider_slug: navision
schema_file: json-schema/admin-center-create-environment-request-schema.json
slug: admin-center-create-environment-request
tags:
- Business Management
- Dynamics NAV
- ERP
- Finance
- Inventory
- Microsoft
- Navision
title: CreateEnvironmentRequest
---
