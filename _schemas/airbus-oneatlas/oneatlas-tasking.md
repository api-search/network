---
description: ''
layout: schema
name: tasking
properties_list:
- description: The contract id
  name: contractId
  type: object
- description: The order id
  name: orderId
  type: object
- description: The product type id
  name: productTypeId
  type: object
- description: The customer id
  name: customerId
  type: object
- description: The tasking id
  name: taskingId
  type: string
- description: The segment id
  name: segmentId
  type: object
- description: The licence id
  name: licenceId
  type: object
- description: The quotation id
  name: quotationId
  type: object
- description: ICR's list
  name: taskingIds
  type: array
- description: Number of items per page
  name: count
  type: integer
- description: Customer reference
  name: customerRef
  type: string
- description: Program name
  name: program
  type: string
- description: ICR Status
  name: status
  type: array
- description: mission name
  name: mission
  type: string
- description: Refer to one-tasking online documentation at http://www.intelligence-airbusds.com/ for more information
  name: progTypeNames
  type: string
- description: 'A date or date interval that must match the product acquisition date. Only taskings in this range are returned in the response. Example: [2017-01-01,2017-02-01[ to select all taskings done in January '
  name: acquisitionDate
  type: string
- description: 'A date or date interval that must match the icr end of period date. Only taskings in this range are returned in the response. Example: [2017-01-01,2017-02-01[ to select all taskings done in January 20'
  name: icrEndOfPeriodDate
  type: string
- description: Indicates whether the search should filter on proposed segments. If set to true, only ICR with proposed segments should be returned. If set to false, only ICR with no proposed segments. If not set, re
  name: hasProposedSegments
  type: boolean
- description: The desired page, starting from 1 for the first page.
  name: startPage
  type: integer
- description: 'A sorting request to the server conforming the OpenSearch SRU specification. Example: sortKeys=acquisitionDate,,0 meaning a request to sort by newest acquired image first or sortKeys=cloudCover,,1 to '
  name: sortKeys
  type: string
provider_name: Airbus OneAtlas
provider_slug: airbus-oneatlas
schema_file: json-schema/oneatlas-tasking-schema.json
slug: oneatlas-tasking
tags:
- Imagery
- Satellites
title: tasking
---
