---
description: JSON Schema for an SAP Ariba Purchase Order document representing a buyer's commitment to purchase goods or services from a supplier through the SAP Business Network. Based on the SAP Ariba Procurement API data model documented at https://help.sap.com/docs/ariba-apis and the Purchase Order web service schemas.
layout: schema
name: SAP Ariba Purchase Order
properties_list:
- description: Unique purchase order identifier (UniqueName) including version number. This is the primary key for the purchase order in SAP Ariba.
  name: orderId
  type: string
- description: ERP system purchase order number (ERPPONumber). Defines the unique ID for every version of the purchase order in the backend ERP system.
  name: erpPONumber
  type: string
- description: Supplemental version number of the original order. Incremented with each change request or modification.
  name: versionNumber
  type: integer
- description: Date and time when the purchase order was created (ISO 8601 format).
  name: orderDate
  type: string
- description: Current status of the purchase order in the procurement lifecycle.
  name: status
  type: string
- description: Defines the ordering method category for the purchase order indicating how it was generated (e.g., manual entry, automatic from requisition, blanket release).
  name: orderMethodCategory
  type: string
- description: The supplier from whom goods or services are being purchased.
  name: supplier
  type: object
- description: The buyer organization placing the purchase order.
  name: buyer
  type: object
- description: ISO 4217 currency code defining the type of currency used for the purchase order.
  name: currency
  type: string
- description: Total monetary value of the purchase order including all line items.
  name: totalAmount
  type: object
- description: Total tax amount for the purchase order.
  name: taxAmount
  type: object
- description: Total shipping and handling charges.
  name: shippingAmount
  type: object
- description: Payment terms governing when and how invoices against this order should be paid. References the unique payment terms code assigned to the supplier.
  name: paymentTerms
  type: object
- description: Purchasing organization identifier (PurchaseOrg/UniqueName). Defines the unique purchase organization responsible for this order.
  name: purchaseOrg
  type: string
- description: Purchasing group identifier (PurchaseGroup/UniqueName). Defines the unique purchase group handling this order.
  name: purchaseGroup
  type: string
- description: Company code for the buying legal entity.
  name: companyCode
  type: string
- description: Default shipping address for the purchase order. Can be overridden at the line item level.
  name: shipTo
  type: object
- description: Billing address for invoice submission.
  name: billTo
  type: object
- description: Line items contained in the purchase order. Each line item represents a specific good or service being procured.
  name: lineItems
  type: array
- description: Line items that have been deleted in a change order. Contains the line numbers of removed items.
  name: deletedLineItems
  type: array
- description: Reference to the originating purchase requisition that generated this order.
  name: requisitionId
  type: string
- description: Reference to a master agreement or contract against which this order is placed.
  name: contractId
  type: string
- description: Header-level comments or notes on the purchase order.
  name: comments
  type: string
- description: Structured header text elements for SAP integration.
  name: headerText
  type: array
- description: Custom field extensions for organization-specific data requirements.
  name: customFields
  type: object
- description: Timestamp when the order was first created in the system.
  name: createdDate
  type: string
- description: Timestamp of the most recent modification.
  name: lastModifiedDate
  type: string
- description: Timestamp when the order was closed.
  name: closedDate
  type: string
provider_name: SAP Ariba
provider_slug: sap-ariba
schema_file: json-schema/sap-ariba-purchase-order-schema.json
slug: sap-ariba-purchase-order
tags:
- B2B
- Contract Management
- Procurement
- Sourcing
- Spend Analysis
- Supplier Management
- Supply Chain
title: SAP Ariba Purchase Order
---
