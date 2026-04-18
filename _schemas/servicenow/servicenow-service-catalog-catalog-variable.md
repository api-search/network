---
description: A variable on a catalog item form.
layout: schema
name: CatalogVariable
properties_list:
- description: The internal name of the variable.
  name: name
  type: string
- description: The display label.
  name: label
  type: string
- description: The variable type.
  name: type
  type: string
- description: Whether the variable is required.
  name: mandatory
  type: boolean
- description: The default value.
  name: default_value
  type: string
- description: Available choices for select-type variables.
  name: choices
  type: array
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-service-catalog-catalog-variable-schema.json
slug: servicenow-service-catalog-catalog-variable
tags:
- Automation
- Cloud Services
- Digital Workflows
- Enterprise Platform
- IT Service Management
- ITSM
- Processes
- T1
- Workflow Automation
- Workflows
title: CatalogVariable
---
