---
description: A purchase requisition requesting procurement of goods or services
layout: schema
name: Requisition
properties_list:
- description: Unique requisition identifier
  name: requisitionId
  type: string
- description: Requisition title or name
  name: title
  type: string
- description: User ID of the person who created the requisition
  name: requestor
  type: string
- description: Full name of the requestor
  name: requestorName
  type: string
- description: Department of the requestor
  name: department
  type: string
- description: Company code
  name: companyCode
  type: string
- description: Desired delivery date
  name: needByDate
  type: string
- description: ''
  name: lineItems
  type: array
- description: Purchase order IDs generated from this requisition after approval
  name: purchaseOrderIds
  type: array
- description: Requisition comments
  name: comments
  type: string
- description: ''
  name: createdDate
  type: string
- description: ''
  name: lastModifiedDate
  type: string
- description: ''
  name: approvedDate
  type: string
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-procurement-requisition-schema.json
slug: sap-ariba-procurement-requisition
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: Requisition
---
