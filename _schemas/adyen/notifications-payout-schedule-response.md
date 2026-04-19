---
description: PayoutScheduleResponse schema from Adyen API
layout: schema
name: PayoutScheduleResponse
properties_list:
- description: The date of the next scheduled payout.
  name: nextScheduledPayout
  type: string
- description: 'The payout schedule of the account. Permitted values: `DEFAULT`, `DAILY`, `DAILY_US`, `DAILY_EU`, `DAILY_AU`, `DAILY_SG`, `WEEKLY`, `WEEKLY_ON_TUE_FRI_MIDNIGHT`, `BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT`'
  name: schedule
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-payout-schedule-response-schema.json
slug: notifications-payout-schedule-response
tags:
- Payments
- Financial Services
- Fintech
title: PayoutScheduleResponse
---
