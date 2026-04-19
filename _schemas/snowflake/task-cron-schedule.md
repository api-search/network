---
description: A cron schedule for executing a task at a specified interval.
layout: schema
name: CronSchedule
properties_list:
- description: A cron expression for the task execution.
  name: cron_expr
  type: string
- description: The time zone for the schedule.
  name: timezone
  type: string
provider_name: Snowflake
provider_slug: snowflake
schema_file: json-schema/task-cron-schedule-schema.json
slug: task-cron-schedule
tags:
- Data Lakes
- Data Sharing
- Data Warehousing
- Database
- SQL
title: CronSchedule
---
