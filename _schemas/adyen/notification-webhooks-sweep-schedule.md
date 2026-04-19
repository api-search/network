---
description: SweepSchedule schema from Adyen API
layout: schema
name: SweepSchedule
properties_list:
- description: 'The schedule type. Possible values: * **cron**: push out funds based on a cron expression. * **daily**: push out funds daily at 07:00 AM CET. * **weekly**: push out funds every Monday at 07:00 AM CET.'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-sweep-schedule-schema.json
slug: notification-webhooks-sweep-schedule
tags:
- Payments
- Financial Services
- Fintech
title: SweepSchedule
---
