---
description: ''
layout: schema
name: DiscreteJob
properties_list:
- description: WIP entity identifier
  name: wipEntityId
  type: integer
- description: Job name/number
  name: wipEntityName
  type: string
- description: Organization identifier
  name: organizationId
  type: integer
- description: Primary assembly item identifier
  name: primaryItemId
  type: integer
- description: Primary assembly item number
  name: primaryItemNumber
  type: string
- description: Job status (1=Unreleased, 3=Released, 4=Complete, 5=Complete-No Charges, 6=On Hold, 7=Cancelled, 12=Closed, 14=Pending Close, 15=Failed Close)
  name: statusType
  type: integer
- description: Job type (1=Standard, 3=Non-Standard)
  name: jobType
  type: integer
- description: Start quantity
  name: startQuantity
  type: number
- description: Quantity completed
  name: quantityCompleted
  type: number
- description: Quantity scrapped
  name: quantityScrapped
  type: number
- description: Net quantity remaining
  name: netQuantity
  type: number
- description: Scheduled start date
  name: scheduledStartDate
  type: string
- description: Scheduled completion date
  name: scheduledCompletionDate
  type: string
- description: Date released
  name: dateReleased
  type: string
- description: Date completed
  name: dateCompleted
  type: string
- description: Date closed
  name: dateClosed
  type: string
- description: Accounting class code
  name: classCode
  type: string
- description: BOM revision
  name: bomRevision
  type: string
- description: Routing revision
  name: routingRevision
  type: string
- description: Job description
  name: description
  type: string
- description: Firm planned flag (1=Firm, 2=Not Firm)
  name: firmPlannedFlag
  type: integer
- description: ''
  name: creationDate
  type: string
- description: ''
  name: lastUpdateDate
  type: string
provider_name: Oracle E-Business Suite
provider_slug: oracle-e-business-suite
schema_file: json-schema/manufacturing-discrete-job-schema.json
slug: manufacturing-discrete-job
tags:
- Business Applications
- E-Business Suite
- Enterprise
- ERP
- Oracle
title: DiscreteJob
---
