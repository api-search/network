---
description: ''
layout: schema
name: Dpas
properties_list:
- description: The registered identifier for the Digital Payment Application (DPA) accessing the service. At least one DPA needs to be registered for each Merchant/Merchant OBO/Sub-Merchant (PF) needed, with additio
  name: srcDpaId
  type: string
- description: Indicates if the Digital Payment Application (DPA) has an Acquirer relationship. This field may be used to improve acceptance rates.
  name: hasAcquirerRelationship
  type: string
- description: Identifier assigned to a Sub-Merchant by the Payment Facilitator (PF). This field may be used to improve transaction security and acceptance rates.
  name: subMerchantId
  type: string
- description: Payment Facilitator (PF) identifier that may be used to improve transaction security and acceptance rates.
  name: paymentFacilitatorId
  type: string
- description: 'Conditional: Must be set to true when the Digital Payment Application (DPA) processes in the United States (US) under the Click to Pay (C2P) program.'
  name: debitTokenRequested
  type: boolean
- description: Object for the array of Merchant Category Codes (MCC) that the Merchant processes transactions under, and is used for risk-scoring transactions by the issuer. All MCC codes that will be processed by a
  name: merchantCategoryCodes
  type: array
- description: ''
  name: acquirerData
  type: array
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-checkout-solutions-dpas-schema.json
slug: mastercard-checkout-solutions-dpas
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Dpas
---
