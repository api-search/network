---
description: ''
layout: schema
name: AgreementAckForAgmtRetrieval
properties_list:
- description: Unique identifier assigned by Mastercard to the agreement.
  name: agreementId
  type: string
- description: Creditor requesting DSP to display to Debtor to setup Agreement during payment confirmation. * Refer to Codes and Formats section for more details.
  name: agreementType
  type: string
- description: Status of the Agreement. * Refer to Codes and Formats section for more details.
  name: agreementStatus
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-debtor-service-provider-resources-agreement-ack-for-agmt-retrieval-schema.json
slug: mastercard-debtor-service-provider-resources-agreement-ack-for-agmt-retrieval
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: AgreementAckForAgmtRetrieval
---
