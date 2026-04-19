---
description: AssignTerminalsRequest schema from Adyen API
layout: schema
name: AssignTerminalsRequest
properties_list:
- description: Your company account. To return terminals to the company inventory, specify only this parameter and the `terminals`.
  name: companyAccount
  type: string
- description: Name of the merchant account. Specify this parameter to assign terminals to this merchant account or to a store under this merchant account.
  name: merchantAccount
  type: string
- description: Boolean that indicates if you are assigning the terminals to the merchant inventory. Do not use when assigning terminals to a store. Required when assigning the terminal to a merchant account. - Set t
  name: merchantInventory
  type: boolean
- description: The store code of the store that you want to assign the terminals to.
  name: store
  type: string
- description: Array containing a list of terminal IDs that you want to assign or reassign to the merchant account or store, or that you want to return to the company inventory. For example, `["V400m-324689776","P40
  name: terminals
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/pos-terminal-assign-terminals-request-schema.json
slug: pos-terminal-assign-terminals-request
tags:
- Payments
- Financial Services
- Fintech
title: AssignTerminalsRequest
---
