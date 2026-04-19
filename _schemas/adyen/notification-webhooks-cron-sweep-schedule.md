---
description: CronSweepSchedule schema from Adyen API
layout: schema
name: CronSweepSchedule
properties_list:
- description: A [cron expression](https://en.wikipedia.org/wiki/Cron#CRON_expression) that is used to set the sweep schedule. The schedule uses the time zone of the balance account. For example, **30 17 * * MON** s
  name: cronExpression
  type: string
- description: 'The schedule type. Possible values: * **cron**: push out funds based on a cron expression. * **daily**: push out funds daily at 07:00 AM CET. * **weekly**: push out funds every Monday at 07:00 AM CET.'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-cron-sweep-schedule-schema.json
slug: notification-webhooks-cron-sweep-schedule
tags:
- Payments
- Financial Services
- Fintech
title: CronSweepSchedule
---
