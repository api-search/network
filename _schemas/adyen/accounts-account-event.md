---
description: AccountEvent schema from Adyen API
layout: schema
name: AccountEvent
properties_list:
- description: 'The event. >Permitted values: `InactivateAccount`, `RefundNotPaidOutTransfers`. For more information, refer to [Verification checks](https://docs.adyen.com/marketplaces-and-platforms/classic/verificat'
  name: event
  type: string
- description: The date on which the event will take place.
  name: executionDate
  type: string
- description: The reason why this event has been created.
  name: reason
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-account-event-schema.json
slug: accounts-account-event
tags:
- Payments
- Financial Services
- Fintech
title: AccountEvent
---
