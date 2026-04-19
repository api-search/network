---
description: Library analytics variable usage data broken down by variable.
layout: schema
name: LibraryAnalyticsVariableUsagesByAsset
properties_list:
- description: Unique, stable id of the variable.
  name: variableKey
  type: string
- description: The name of the variable.
  name: variableName
  type: string
- description: The type of the variable.
  name: variableType
  type: string
- description: Unique, stable id of the collection the variable belongs to.
  name: collectionKey
  type: string
- description: The name of the collection the variable belongs to.
  name: collectionName
  type: string
- description: The number of usages of the variable within the organization.
  name: usages
  type: number
- description: The number of teams using the variable within the organization.
  name: teamsUsing
  type: number
- description: The number of files using the variable within the organization.
  name: filesUsing
  type: number
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-analytics-library-analytics-variable-usages-by-asset-schema.json
slug: figma-analytics-library-analytics-variable-usages-by-asset
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: LibraryAnalyticsVariableUsagesByAsset
---
