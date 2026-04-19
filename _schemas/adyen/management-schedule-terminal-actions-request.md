---
description: ScheduleTerminalActionsRequest schema from Adyen API
layout: schema
name: ScheduleTerminalActionsRequest
properties_list:
- description: Information about the action to take.
  name: actionDetails
  type: object
- description: 'The date and time when the action should happen. Format: [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339), but without the **Z** before the time offset. For example, **2021-11-15T12:16:21+01:00** Th'
  name: scheduledAt
  type: string
- description: The unique ID of the [store](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/stores). If present, all terminals in the `terminalIds` list must be assigned to this store.
  name: storeId
  type: string
- description: A list of unique IDs of the terminals to apply the action to. You can extract the IDs from the [GET `/terminals`](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/terminals) response
  name: terminalIds
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-schedule-terminal-actions-request-schema.json
slug: management-schedule-terminal-actions-request
tags:
- Payments
- Financial Services
- Fintech
title: ScheduleTerminalActionsRequest
---
