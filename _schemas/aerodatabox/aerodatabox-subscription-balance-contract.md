---
description: Represents the balance for all alert subscriptions associated with the user acount, including remaining credits and timestamps for the most recent refill and deduction operations.
layout: schema
name: SubscriptionBalanceContract
properties_list:
- description: Alert credits remaining for the account.
  name: creditsRemaining
  type: integer
- description: The datetime when the balance was last re-filled, in UTC.
  name: lastRefilledUtc
  type: string
- description: The datetime when the balance was last deducated, in UTC. Deduction typically occurs when an alert notification was dispatched for one of the alert subscriptions associated with the user account.
  name: lastDeductedUtc
  type: string
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-subscription-balance-contract-schema.json
slug: aerodatabox-subscription-balance-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: SubscriptionBalanceContract
---
