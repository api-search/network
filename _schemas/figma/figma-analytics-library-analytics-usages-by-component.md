---
description: Library analytics usage data broken down by component.
layout: schema
name: LibraryAnalyticsUsagesByComponent
properties_list:
- description: Unique, stable id of the component.
  name: componentKey
  type: string
- description: Name of the component.
  name: componentName
  type: string
- description: Unique, stable id of the component set that this component belongs to.
  name: componentSetKey
  type: string
- description: Name of the component set that this component belongs to.
  name: componentSetName
  type: string
- description: The number of instances of the component within the organization.
  name: numInstances
  type: number
- description: The number of teams using the component within the organization.
  name: numTeamsUsing
  type: number
- description: The number of files using the component within the organization.
  name: numFilesUsing
  type: number
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-analytics-library-analytics-usages-by-component-schema.json
slug: figma-analytics-library-analytics-usages-by-component
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: LibraryAnalyticsUsagesByComponent
---
