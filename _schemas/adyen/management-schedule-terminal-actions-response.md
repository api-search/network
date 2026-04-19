---
description: ScheduleTerminalActionsResponse schema from Adyen API
layout: schema
name: ScheduleTerminalActionsResponse
properties_list:
- description: Information about the action to take.
  name: actionDetails
  type: object
- description: A list containing a terminal ID and an action ID for each terminal that the action was scheduled for.
  name: items
  type: array
- description: 'The date and time when the action should happen. Format: [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339), but without the **Z** before the time offset. For example, **2021-11-15T12:16:21+01:00** Th'
  name: scheduledAt
  type: string
- description: The unique ID of the [store](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/stores). If present, all terminals in the `terminalIds` list must be assigned to this store.
  name: storeId
  type: string
- description: The validation errors that occurred in the list of terminals, and for each error the IDs of the terminals that the error applies to.
  name: terminalsWithErrors
  type: object
- description: The number of terminals for which scheduling the action failed.
  name: totalErrors
  type: integer
- description: The number of terminals for which the action was successfully scheduled. This doesn't mean the action has happened yet.
  name: totalScheduled
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-schedule-terminal-actions-response-schema.json
slug: management-schedule-terminal-actions-response
tags:
- Payments
- Financial Services
- Fintech
title: ScheduleTerminalActionsResponse
---
