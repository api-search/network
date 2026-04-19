---
description: ExternalTerminalAction schema from Adyen API
layout: schema
name: ExternalTerminalAction
properties_list:
- description: 'The type of terminal action: **InstallAndroidApp**, **UninstallAndroidApp**, **InstallAndroidCertificate**, or **UninstallAndroidCertificate**.'
  name: actionType
  type: string
- description: Technical information about the terminal action.
  name: config
  type: string
- description: The date and time when the action was carried out.
  name: confirmedAt
  type: string
- description: The unique ID of the terminal action.
  name: id
  type: string
- description: The result message for the action.
  name: result
  type: string
- description: The date and time when the action was scheduled to happen.
  name: scheduledAt
  type: string
- description: 'The status of the terminal action: **pending**, **successful**, **failed**, **cancelled**, or **tryLater**.'
  name: status
  type: string
- description: The unique ID of the terminal that the action applies to.
  name: terminalId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-external-terminal-action-schema.json
slug: management-external-terminal-action
tags:
- Payments
- Financial Services
- Fintech
title: ExternalTerminalAction
---
