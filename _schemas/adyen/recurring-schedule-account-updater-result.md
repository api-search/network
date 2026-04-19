---
description: ScheduleAccountUpdaterResult schema from Adyen API
layout: schema
name: ScheduleAccountUpdaterResult
properties_list:
- description: Adyen's 16-character unique reference associated with the transaction. This value is globally unique; quote it when communicating with us about this request.
  name: pspReference
  type: string
- description: The result of scheduling an Account Updater. If scheduling was successful, this field returns **Success**; otherwise it contains the error message.
  name: result
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/recurring-schedule-account-updater-result-schema.json
slug: recurring-schedule-account-updater-result
tags:
- Payments
- Financial Services
- Fintech
title: ScheduleAccountUpdaterResult
---
