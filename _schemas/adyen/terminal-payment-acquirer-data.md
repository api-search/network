---
description: Data related to the response from the payment Acquirer.
layout: schema
name: PaymentAcquirerData
properties_list:
- description: If several Acquirers.
  name: AcquirerID
  type: integer
- description: Identification of the Merchant for the Acquirer.
  name: MerchantID
  type: string
- description: Identification of the POI for the payment Acquirer.
  name: AcquirerPOIID
  type: string
- description: ''
  name: AcquirerTransactionID
  type: object
- description: If available.
  name: ApprovalCode
  type: string
- description: ''
  name: HostReconciliationID
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-payment-acquirer-data-schema.json
slug: terminal-payment-acquirer-data
tags:
- Payments
- Financial Services
- Fintech
title: PaymentAcquirerData
---
