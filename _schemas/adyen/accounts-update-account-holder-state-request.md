---
description: UpdateAccountHolderStateRequest schema from Adyen API
layout: schema
name: UpdateAccountHolderStateRequest
properties_list:
- description: The code of the Account Holder on which to update the state.
  name: accountHolderCode
  type: string
- description: If true, disable the requested state. If false, enable the requested state.
  name: disable
  type: boolean
- description: The reason that the state is being updated. >Required if the state is being disabled.
  name: reason
  type: string
- description: 'The state to be updated. >Permitted values are: `Processing`, `Payout`'
  name: stateType
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-update-account-holder-state-request-schema.json
slug: accounts-update-account-holder-state-request
tags:
- Payments
- Financial Services
- Fintech
title: UpdateAccountHolderStateRequest
---
