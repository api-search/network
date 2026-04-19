---
description: DeleteShareholderRequest schema from Adyen API
layout: schema
name: DeleteShareholderRequest
properties_list:
- description: The code of the Account Holder from which to delete the Shareholders.
  name: accountHolderCode
  type: string
- description: The code(s) of the Shareholders to be deleted.
  name: shareholderCodes
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-delete-shareholder-request-schema.json
slug: accounts-delete-shareholder-request
tags:
- Payments
- Financial Services
- Fintech
title: DeleteShareholderRequest
---
