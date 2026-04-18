---
consumed_apis:
- mastercom
- processing-core
- ethoca-consumer-clarity
- currency-conversion
description: Unified workflow for dispute managers and back-office teams to manage chargebacks, retrieval requests, transaction processing, and settlement through Mastercom and processing APIs.
layout: capability
name: Mastercard Disputes and Settlement
operations:
- description: Create a chargeback
  method: POST
  name: create-chargeback
  path: /v1/chargebacks
- description: Retrieve chargebacks
  method: GET
  name: get-chargebacks
  path: /v1/chargebacks
- description: Create a retrieval request
  method: POST
  name: create-retrieval
  path: /v1/retrievals
- description: Look up transaction details for dispute resolution
  method: POST
  name: lookup-transaction-clarity
  path: /v1/transaction-clarity
personas: []
provider_name: Mastercard
provider_slug: mastercard
search_terms:
- create a chargeback in mastercom
- get settlement rate
- credit cards
- authorize a transaction through core processing
- create retrieval request
- get currency conversion rate for settlement
- lookup transaction for dispute
- mastercom
- transaction clarity for dispute resolution
- settlement
- financial services
- mastercard
- create a retrieval request
- payments
- retrieve chargebacks
- chargebacks
- digital identity
- open banking
- fraud detection
- chargeback management
- look up transaction details to aid dispute resolution
- disputes
- create a retrieval request in mastercom
- authorize transaction
- create chargeback
- retrieve chargebacks from mastercom
- create retrieval
- look up transaction details for dispute resolution
- retrieval request management
- create a chargeback
- get chargebacks
- lookup transaction clarity
slug: disputes-and-settlement
tags:
- Mastercard
- Disputes
- Chargebacks
- Settlement
- Mastercom
tools:
- description: Create a chargeback in Mastercom
  hints:
    readOnly: false
  name: create-chargeback
- description: Retrieve chargebacks from Mastercom
  hints:
    readOnly: true
  name: get-chargebacks
- description: Create a retrieval request in Mastercom
  hints:
    readOnly: false
  name: create-retrieval-request
- description: Look up transaction details to aid dispute resolution
  hints:
    readOnly: true
  name: lookup-transaction-for-dispute
- description: Authorize a transaction through core processing
  hints:
    readOnly: false
  name: authorize-transaction
- description: Get currency conversion rate for settlement
  hints:
    idempotent: true
    readOnly: true
  name: get-settlement-rate
---
