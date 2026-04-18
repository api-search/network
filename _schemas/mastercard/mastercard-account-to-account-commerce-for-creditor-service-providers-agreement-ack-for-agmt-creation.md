---
description: ''
layout: schema
name: AgreementAckForAgmtCreation
properties_list:
- description: Unique identifier assigned by Mastercard to the agreement.
  name: agreementId
  type: string
- description: Agreement Status returned by Mastercard. * Refer to Codes and Formats section for more details.
  name: agreementStatus
  type: string
- description: Unique 6 digit reference provided by Mastercard to the CSP to be conveyed to the Debtor in order to create an agreement.
  name: agreementReferenceNumber
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-account-to-account-commerce-for-creditor-service-providers-agreement-ack-for-agmt-creation-schema.json
slug: mastercard-account-to-account-commerce-for-creditor-service-providers-agreement-ack-for-agmt-creation
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: AgreementAckForAgmtCreation
---
