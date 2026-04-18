---
description: The result of processing an import set record including the transformation outcome.
layout: schema
name: ImportSetResult
properties_list:
- description: The name of the transform map used to process the record.
  name: transform_map
  type: string
- description: The target table into which the record was transformed.
  name: table
  type: string
- description: The display name of the transform map.
  name: display_name
  type: string
- description: The display value of the target record created or updated.
  name: display_value
  type: string
- description: A link to the target record in ServiceNow.
  name: record_link
  type: string
- description: The transformation status. Common values include inserted, updated, error, and ignored.
  name: status
  type: string
- description: A descriptive message about the transformation result, especially useful when the status is error.
  name: status_message
  type: string
- description: The sys_id of the import set row record in the staging table.
  name: sys_id
  type: string
- description: The sys_id of the record created or updated in the target table.
  name: target_sys_id
  type: string
- description: The sys_id of the parent import set.
  name: import_set
  type: string
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-import-set-import-set-result-schema.json
slug: servicenow-import-set-import-set-result
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
title: ImportSetResult
---
