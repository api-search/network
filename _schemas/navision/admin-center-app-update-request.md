---
description: ''
layout: schema
name: AppUpdateRequest
properties_list:
- description: Target version to update to
  name: targetVersion
  type: string
- description: Whether to allow preview versions
  name: allowPreviewVersion
  type: boolean
- description: Whether to ignore the update window
  name: ignoreUpgradeWindow
  type: boolean
- description: Whether to also update dependent apps
  name: allowDependencyUpdate
  type: boolean
provider_name: Microsoft Dynamics NAV
provider_slug: navision
schema_file: json-schema/admin-center-app-update-request-schema.json
slug: admin-center-app-update-request
tags:
- Business Management
- Dynamics NAV
- ERP
- Finance
- Inventory
- Microsoft
- Navision
title: AppUpdateRequest
---
