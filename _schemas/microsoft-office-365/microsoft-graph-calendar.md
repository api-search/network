---
description: A calendar which is a container for events.
layout: schema
name: Calendar
properties_list:
- description: The unique identifier for the calendar.
  name: id
  type: string
- description: The calendar name.
  name: name
  type: string
- description: Specifies the color theme for the calendar.
  name: color
  type: string
- description: Identifies the version of the calendar object.
  name: changeKey
  type: string
- description: Whether the user can write to the calendar.
  name: canEdit
  type: boolean
- description: Whether the user has permission to share the calendar.
  name: canShare
  type: boolean
- description: Whether the user can read calendar items marked as private.
  name: canViewPrivateItems
  type: boolean
- description: Whether this is the default calendar.
  name: isDefaultCalendar
  type: boolean
- description: The calendar color expressed in hex format of three six-digit values.
  name: hexColor
  type: string
- description: Whether the calendar can be deleted from the user's mailbox.
  name: isRemovable
  type: boolean
- description: Whether the calendar supports tracking of meeting responses.
  name: isTallyingResponses
  type: boolean
- description: The online meeting service providers available for events in this calendar.
  name: allowedOnlineMeetingProviders
  type: array
- description: The default online meeting provider for meetings sent from this calendar.
  name: defaultOnlineMeetingProvider
  type: string
provider_name: Microsoft Office 365
provider_slug: microsoft-office-365
schema_file: json-schema/microsoft-graph-calendar-schema.json
slug: microsoft-graph-calendar
tags:
- Cloud
- Collaboration
- Enterprise
- Microsoft
- Productivity
title: Calendar
---
