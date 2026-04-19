---
description: TransactionRuleInterval schema from Adyen API
layout: schema
name: TransactionRuleInterval
properties_list:
- description: The day of month, used when the `duration.unit` is **months**. If not provided, by default, this is set to **1**, the first day of the month.
  name: dayOfMonth
  type: integer
- description: 'The day of week, used when the `duration.unit` is **weeks**. If not provided, by default, this is set to **monday**. Possible values: **sunday**, **monday**, **tuesday**, **wednesday**, **thursday**, '
  name: dayOfWeek
  type: string
- description: The duration, which you can specify in hours, days, weeks, or months. The maximum duration is 90 days or an equivalent in other units. Required when the `type` is **rolling** or **sliding**.
  name: duration
  type: object
- description: The time of day, in **hh:mm:ss** format, used when the `duration.unit` is **hours**. If not provided, by default, this is set to **00:00:00**.
  name: timeOfDay
  type: string
- description: The [time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). For example, **Europe/Amsterdam**. By default, this is set to **UTC**.
  name: timeZone
  type: string
- description: 'The [type of interval](https://docs.adyen.com/issuing/transaction-rules#time-intervals) during which the rule conditions and limits apply, and how often counters are reset. Possible values: * **perTra'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-transaction-rule-interval-schema.json
slug: configuration-transaction-rule-interval
tags:
- Payments
- Financial Services
- Fintech
title: TransactionRuleInterval
---
