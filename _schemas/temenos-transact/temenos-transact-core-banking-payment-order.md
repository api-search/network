---
description: A payment order in Temenos Transact for submitting payment instructions through various clearing systems.
layout: schema
name: PaymentOrder
properties_list:
- description: Unique payment order identifier
  name: paymentOrderId
  type: string
- description: Debit account identifier
  name: debitAccountId
  type: string
- description: Amount debited from the source account
  name: debitAmount
  type: number
- description: Currency of the debit
  name: debitCurrency
  type: string
- description: Credit account identifier or beneficiary account
  name: creditAccountId
  type: string
- description: Amount credited to the destination account
  name: creditAmount
  type: number
- description: Currency of the credit
  name: creditCurrency
  type: string
- description: Payment type classification
  name: paymentType
  type: string
- description: Payment order status
  name: status
  type: string
- description: Value date of the payment
  name: valueDate
  type: string
- description: Timestamp when the payment was executed
  name: executionDate
  type: string
- description: Name of the payment beneficiary
  name: beneficiaryName
  type: string
- description: IBAN of the beneficiary
  name: beneficiaryIban
  type: string
- description: BIC/SWIFT code of the beneficiary bank
  name: beneficiaryBic
  type: string
- description: Remittance information or payment reference
  name: remittanceInformation
  type: string
- description: Who bears the charges
  name: chargesType
  type: string
- description: Total charges applied
  name: totalCharges
  type: number
- description: Applied exchange rate
  name: exchangeRate
  type: number
- description: Reason for rejection if applicable
  name: rejectionReason
  type: string
provider_name: Temenos Transact
provider_slug: temenos-transact
schema_file: json-schema/temenos-transact-core-banking-payment-order-schema.json
slug: temenos-transact-core-banking-payment-order
tags:
- Banking
- Core Banking
- Digital Banking
- Enterprise
- Financial Services
- Fintech
title: PaymentOrder
---
