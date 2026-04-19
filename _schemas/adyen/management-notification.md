---
description: Notification schema from Adyen API
layout: schema
name: Notification
properties_list:
- description: The type of event notification sent when you select the notification button.
  name: category
  type: string
- description: The text shown in the prompt which opens when you select the notification button. For example, the description of the input box for pay-at-table.
  name: details
  type: string
- description: Enables sending event notifications either by pressing the Confirm key on terminals with a keypad or by tapping the event notification button on the terminal screen.
  name: enabled
  type: boolean
- description: Shows or hides the event notification button on the screen of terminal models that have a keypad.
  name: showButton
  type: boolean
- description: The name of the notification button on the terminal screen.
  name: title
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-notification-schema.json
slug: management-notification
tags:
- Payments
- Financial Services
- Fintech
title: Notification
---
