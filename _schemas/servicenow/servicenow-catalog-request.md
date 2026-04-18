---
description: A ServiceNow service catalog request record representing a user's request for one or more catalog items through the self-service portal.
layout: schema
name: ServiceNow Catalog Request
properties_list:
- description: The unique 32-character system identifier for the request.
  name: sys_id
  type: string
- description: The human-readable request number, prefixed with REQ.
  name: number
  type: string
- description: The current state of the request.
  name: request_state
  type: string
- description: The current stage of the request in the fulfillment workflow.
  name: stage
  type:
  - string
  - 'null'
- description: The user for whom the catalog items were requested.
  name: requested_for
  type: object
- description: The user who submitted the request.
  name: opened_by
  type: object
- description: The date and time the request was submitted.
  name: opened_at
  type: string
- description: The delivery address for physical items.
  name: delivery_address
  type:
  - string
  - 'null'
- description: Special instructions provided by the requester.
  name: special_instructions
  type:
  - string
  - 'null'
- description: The total price for all requested items.
  name: price
  type:
  - string
  - 'null'
- description: The current approval status of the request.
  name: approval
  type:
  - string
  - 'null'
- description: The line items in this request.
  name: requested_items
  type: array
- description: Whether the request is still active.
  name: active
  type: boolean
- description: The date and time the record was created.
  name: sys_created_on
  type: string
- description: The user who created the record.
  name: sys_created_by
  type: string
- description: The date and time the record was last updated.
  name: sys_updated_on
  type: string
- description: The user who last updated the record.
  name: sys_updated_by
  type: string
provider_name: ServiceNow
provider_slug: servicenow
schema_file: json-schema/servicenow-catalog-request-schema.json
slug: servicenow-catalog-request
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
title: ServiceNow Catalog Request
---
