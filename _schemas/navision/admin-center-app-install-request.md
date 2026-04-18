---
description: ''
layout: schema
name: AppInstallRequest
properties_list:
- description: Version to install
  name: targetVersion
  type: string
- description: Whether to allow preview versions
  name: allowPreviewVersion
  type: boolean
- description: Whether the ISV EULA is accepted
  name: acceptIsvEula
  type: boolean
- description: Whether to also update dependent apps
  name: allowDependencyUpdate
  type: boolean
provider_name: Microsoft Dynamics NAV
provider_slug: navision
schema_file: json-schema/admin-center-app-install-request-schema.json
slug: admin-center-app-install-request
tags:
- Business Management
- Dynamics NAV
- ERP
- Finance
- Inventory
- Microsoft
- Navision
title: AppInstallRequest
---
