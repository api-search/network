---
description: AccountHolderStatus schema from Adyen API
layout: schema
name: AccountHolderStatus
properties_list:
- description: A list of events scheduled for the account holder.
  name: events
  type: array
- description: The payout state of the account holder.
  name: payoutState
  type: object
- description: The processing state of the account holder.
  name: processingState
  type: object
- description: 'The status of the account holder. >Permitted values: `Active`, `Inactive`, `Suspended`, `Closed`.'
  name: status
  type: string
- description: The reason why the status was assigned to the account holder.
  name: statusReason
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-account-holder-status-schema.json
slug: accounts-account-holder-status
tags:
- Payments
- Financial Services
- Fintech
title: AccountHolderStatus
---
