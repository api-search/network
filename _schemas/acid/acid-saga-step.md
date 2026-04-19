---
description: A step in a distributed Saga pattern transaction, representing a local transaction with a compensating action for rollback.
layout: schema
name: AcidSagaStep
properties_list:
- description: Unique identifier for this saga step
  name: stepId
  type: string
- description: Identifier of the parent saga workflow
  name: sagaId
  type: string
- description: Human-readable name for this saga step
  name: stepName
  type: string
- description: Execution order within the saga (1-based)
  name: sequence
  type: integer
- description: Current status of this saga step
  name: status
  type: string
- description: URL of the service responsible for this step
  name: serviceEndpoint
  type: string
- description: URL to call to undo this step if a later step fails
  name: compensationEndpoint
  type: string
- description: When this step began executing
  name: startTime
  type: string
- description: When this step completed or was compensated
  name: endTime
  type: string
- description: Number of retry attempts for this step
  name: retryCount
  type: integer
- description: Error message if the step failed
  name: errorMessage
  type: string
provider_name: ACID
provider_slug: acid
schema_file: json-schema/acid-saga-step-schema.json
slug: acid-saga-step
tags:
- ACID
- Database
- Transactions
- Atomicity
- Consistency
- Isolation
- Durability
- Distributed Systems
title: AcidSagaStep
---
