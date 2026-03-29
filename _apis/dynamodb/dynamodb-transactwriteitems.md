---
aid: dynamodb:dynamodb-transactwriteitems
name: Write items in a transaction
tags:
- Transactions
humanURL: 
properties: []
description: >-
  A synchronous write operation that groups up to 100 action requests. These actions can target items in different tables, but not in different accounts or Regions. The actions are completed atomically so that either all of them succeed, or all of them fail. TransactWriteItems supports Put, Update, Delete, and ConditionCheck actions.

---
