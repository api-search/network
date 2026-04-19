---
description: A public holiday calendar in absentify.
layout: schema
name: PublicHolidayCalendar
properties_list:
- description: Unique identifier of the calendar.
  name: id
  type: string
- description: Name of the public holiday calendar.
  name: name
  type: string
- description: Country code for the public holidays.
  name: country
  type: string
- description: Timestamp when the calendar was created.
  name: createdAt
  type: string
- description: Timestamp when the calendar was last updated.
  name: updatedAt
  type: string
provider_name: Absentify
provider_slug: absentify
schema_file: json-schema/absentify-public-holiday-calendar-schema.json
slug: absentify-public-holiday-calendar
tags:
- Absence Management
- HR
- Leave Management
- Microsoft Teams
- Human Resources
title: PublicHolidayCalendar
---
