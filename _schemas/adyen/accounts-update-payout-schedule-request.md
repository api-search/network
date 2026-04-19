---
description: UpdatePayoutScheduleRequest schema from Adyen API
layout: schema
name: UpdatePayoutScheduleRequest
properties_list:
- description: 'Direction on how to handle any payouts that have already been scheduled. Permitted values: * `CLOSE` will close the existing batch of payouts. * `UPDATE` will reschedule the existing batch to the new '
  name: action
  type: string
- description: The reason for the payout schedule update. > This field is required when the `schedule` parameter is set to `HOLD`.
  name: reason
  type: string
- description: 'The payout schedule to which the account is to be updated. Permitted values: `DAILY`, `DAILY_US`, `DAILY_EU`, `DAILY_AU`, `DAILY_SG`, `WEEKLY`, `WEEKLY_ON_TUE_FRI_MIDNIGHT`, `BIWEEKLY_ON_1ST_AND_15TH_'
  name: schedule
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-update-payout-schedule-request-schema.json
slug: accounts-update-payout-schedule-request
tags:
- Payments
- Financial Services
- Fintech
title: UpdatePayoutScheduleRequest
---
