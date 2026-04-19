---
description: Represents an ACID database transaction with its properties, status, and isolation level.
layout: schema
name: AcidTransaction
properties_list:
- description: Unique identifier for the transaction
  name: transactionId
  type: string
- description: Current status of the transaction
  name: status
  type: string
- description: SQL transaction isolation level
  name: isolationLevel
  type: string
- description: Timestamp when the transaction began
  name: startTime
  type: string
- description: Timestamp when the transaction was committed or rolled back
  name: endTime
  type: string
- description: Transaction duration in milliseconds
  name: durationMs
  type: integer
- description: List of database operations within this transaction
  name: operations
  type: array
- description: Reason for rollback if the transaction was not committed
  name: rollbackReason
  type: string
- description: Named savepoints defined within this transaction
  name: savepoints
  type: array
provider_name: ACID
provider_slug: acid
schema_file: json-schema/acid-transaction-schema.json
slug: acid-transaction
tags:
- ACID
- Database
- Transactions
- Atomicity
- Consistency
- Isolation
- Durability
- Distributed Systems
title: AcidTransaction
---
