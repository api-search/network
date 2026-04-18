---
description: ''
layout: schema
name: RestoreEnvironmentRequest
properties_list:
- description: Name of the new restored environment
  name: EnvironmentName
  type: string
- description: Type of the new environment
  name: EnvironmentType
  type: string
- description: Point in time to restore to (ISO 8601 UTC)
  name: PointInTime
  type: string
- description: Whether to uninstall per-tenant extensions
  name: SkipInstallingPTEs
  type: boolean
- description: Whether to uninstall third-party AppSource apps
  name: SkipInstallingThirdPartyGlobalApps
  type: boolean
- description: Whether to skip execution of cleanup codeunits
  name: SkipEnvironmentCleanup
  type: boolean
provider_name: Microsoft Dynamics NAV
provider_slug: navision
schema_file: json-schema/admin-center-restore-environment-request-schema.json
slug: admin-center-restore-environment-request
tags:
- Business Management
- Dynamics NAV
- ERP
- Finance
- Inventory
- Microsoft
- Navision
title: RestoreEnvironmentRequest
---
