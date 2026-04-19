---
description: It conveys Information related to the event, and possible action (maintenance, message to display). Content of the EventNotification message.
layout: schema
name: EventNotification
properties_list:
- description: Date and time of a transaction for the Sale System, the POI System or the Acquirer.
  name: TimeStamp
  type: string
- description: ''
  name: EventToNotify
  type: object
- description: If present, the Sale logs it for further examination.
  name: EventDetails
  type: string
- description: Mandatory if EventToNotify is Reject, absent in other cases.
  name: RejectedMessage
  type: string
- description: Indicates if the occurred event requires maintenance call or action.
  name: MaintenanceRequiredFlag
  type: boolean
- description: If the language is selected by the Sale System before the request to the POI.
  name: CustomerLanguage
  type: string
- description: ''
  name: DisplayOutput
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-event-notification-schema.json
slug: terminal-event-notification
tags:
- Payments
- Financial Services
- Fintech
title: EventNotification
---
