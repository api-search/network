---
description: Lifecycle state of a source server
layout: schema
name: LifeCycle
properties_list:
- description: Current lifecycle state
  name: state
  type: string
- description: Date/time the server was added to the service
  name: addedToServiceDateTime
  type: string
- description: Date/time the first replication byte was received
  name: firstByteDateTime
  type: string
- description: Elapsed duration of replication
  name: elapsedReplicationDuration
  type: string
- description: Date/time the agent last communicated with the service
  name: lastSeenByServiceDateTime
  type: string
- description: lastTestInitiated
  name: lastTestInitiated
  type: string
- description: lastTestReverted
  name: lastTestReverted
  type: string
- description: lastTestFinalized
  name: lastTestFinalized
  type: string
- description: lastCutoverInitiated
  name: lastCutoverInitiated
  type: string
- description: lastCutoverReverted
  name: lastCutoverReverted
  type: string
- description: lastCutoverFinalized
  name: lastCutoverFinalized
  type: string
provider_name: Amazon Application Migration Service
provider_slug: amazon-application-migration-service
schema_file: json-schema/application-migration-service-life-cycle-schema.json
slug: application-migration-service-life-cycle
tags:
- Amazon Application Migration Service
- Migration
- Lift And Shift
- AWS
- Cloud Migration
title: LifeCycle
---
