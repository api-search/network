---
description: DeletePayoutMethodRequest schema from Adyen API
layout: schema
name: DeletePayoutMethodRequest
properties_list:
- description: The code of the account holder, from which to delete the payout methods.
  name: accountHolderCode
  type: string
- description: The codes of the payout methods to be deleted.
  name: payoutMethodCodes
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-delete-payout-method-request-schema.json
slug: accounts-delete-payout-method-request
tags:
- Payments
- Financial Services
- Fintech
title: DeletePayoutMethodRequest
---
