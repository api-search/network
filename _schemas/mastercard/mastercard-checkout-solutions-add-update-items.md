---
description: ''
layout: schema
name: AddUpdateItems
properties_list:
- description: The action to be performed on the Digital Payment Application (DPA). The selected action will be applied to all DPAs provided in the items list. ADD - Add DPA UPDATE - Update DPA DELETE - Delete DPA N
  name: action
  type: string
- description: 'Conditional: The Customer Identifier (CID) must be passed when the Integrator is acting On-Behalf-Of (OBO) a client, registering through the Mastercard Connect (MC Connect) portal, or participating in'
  name: customerId
  type: string
- description: The Mastercard program that the Integrator would like to add their client(s) to. The Integrator must be enrolled in the program prior to enrolling their client(s). Integrators may view their active pr
  name: programType
  type: string
- description: The Token Requestor Identifier (TRID) should be passed by MDES for Merchants (M4M) Integrators who would like to onboard their M4M TRIDs to be used on Secure Card on File (SCOF).
  name: trid
  type: string
- description: A unique identifier assigned by Mastercard for which tokens are created uniquely for the entity onboarded.
  name: serviceId
  type: string
- description: Assign a category to the sub-merchant group identified in the request. For example, sub-merchants can be grouped by common attributes such as merchant category code (MCC), volume of transactions, or g
  name: category
  type: string
- description: 'The Cardholder facing name of the Merchant. Conditional: Must be supplied when adding Merchants to all Secure Card On File (SECURE_COF) programs.'
  name: programName
  type: string
- description: Dpas Object for Integrator to provide a list of Digital Processing Application (DPA) objects. Each DPA object is used to create a corresponding DPA. A minimum of 1 DPA object (to a maximum of 80 DPA o
  name: dpas
  type: array
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-checkout-solutions-add-update-items-schema.json
slug: mastercard-checkout-solutions-add-update-items
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: AddUpdateItems
---
