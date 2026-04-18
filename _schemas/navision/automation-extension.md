---
description: ''
layout: schema
name: Extension
properties_list:
- description: The extension ID
  name: id
  type: string
- description: The package ID used for install/uninstall operations
  name: packageId
  type: string
- description: The extension display name
  name: displayName
  type: string
- description: The extension publisher
  name: publisher
  type: string
- description: Major version number
  name: versionMajor
  type: integer
- description: Minor version number
  name: versionMinor
  type: integer
- description: Build version number
  name: versionBuild
  type: integer
- description: Revision version number
  name: versionRevision
  type: integer
- description: Whether the extension is currently installed
  name: isInstalled
  type: boolean
- description: How the extension was published
  name: publishedAs
  type: string
provider_name: Microsoft Dynamics NAV
provider_slug: navision
schema_file: json-schema/automation-extension-schema.json
slug: automation-extension
tags:
- Business Management
- Dynamics NAV
- ERP
- Finance
- Inventory
- Microsoft
- Navision
title: Extension
---
