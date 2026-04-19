---
description: Recurrence settings for recurring meetings.
layout: schema
name: Recurrence
properties_list:
- description: Recurrence type. 1 - Daily, 2 - Weekly, 3 - Monthly.
  name: type
  type: integer
- description: Interval at which the meeting recurs. For daily, max 90. For weekly, max 12. For monthly, max 3.
  name: repeat_interval
  type: integer
- description: Days of the week for weekly recurrence. 1-Sunday through 7-Saturday. Comma separated for multiple days.
  name: weekly_days
  type: string
- description: Day of the month for monthly recurrence (1-31).
  name: monthly_day
  type: integer
- description: Week of the month for monthly recurrence. -1 - Last week, 1 - First, 2 - Second, 3 - Third, 4 - Fourth.
  name: monthly_week
  type: integer
- description: Day of the week for monthly recurrence. 1-Sunday through 7-Saturday.
  name: monthly_week_day
  type: integer
- description: Number of times the meeting will recur before ending. Cannot be used with end_date_time. Maximum 365 for daily, 99 for weekly and monthly.
  name: end_times
  type: integer
- description: The end date-time for the recurrence. Cannot be used with end_times.
  name: end_date_time
  type: string
provider_name: Zoom
provider_slug: zoom
schema_file: json-schema/zoom-meeting-recurrence-schema.json
slug: zoom-meeting-recurrence
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
title: Recurrence
---
