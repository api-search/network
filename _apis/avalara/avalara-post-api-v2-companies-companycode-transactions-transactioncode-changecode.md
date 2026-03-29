---
aid: avalara:avalara-post-api-v2-companies-companycode-transactions-transactioncode-changecode
name: ChangeTransactionCode
tags:
- Transactions
humanURL: 
properties: []
description: >-
  Renames a transaction uniquely identified by this URL by changing its `code` value.              This API is available as long as the transaction is in `saved` or `posted` status.  When a transaction is `committed`, it can be modified by using the [AdjustTransaction](https://developer.avalara.com/api-reference/avatax/rest/v2/methods/Transactions/AdjustTransaction/) method.              After this API call succeeds, the transaction will have a new URL matching its new `code`.            ...

---
