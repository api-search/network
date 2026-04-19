---
description: DeleteSignatoriesRequest schema from Adyen API
layout: schema
name: DeleteSignatoriesRequest
properties_list:
- description: The code of the account holder from which to delete the signatories.
  name: accountHolderCode
  type: string
- description: Array of codes of the signatories to be deleted.
  name: signatoryCodes
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-delete-signatories-request-schema.json
slug: accounts-delete-signatories-request
tags:
- Payments
- Financial Services
- Fintech
title: DeleteSignatoriesRequest
---
