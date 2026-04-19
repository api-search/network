---
description: A loan arrangement in Temenos Transact
layout: schema
name: Loan
properties_list:
- description: Unique loan identifier
  name: loanId
  type: string
- description: Customer identifier
  name: customerId
  type: string
- description: Loan product identifier
  name: productId
  type: string
- description: Name of the loan product
  name: productName
  type: string
- description: Original loan principal amount
  name: principalAmount
  type: number
- description: Current outstanding balance
  name: outstandingBalance
  type: number
- description: Loan currency
  name: currency
  type: string
- description: Applied interest rate percentage
  name: interestRate
  type: number
- description: Annual percentage rate (APR)
  name: effectiveRate
  type: number
- description: Date the loan was disbursed
  name: disbursementDate
  type: string
- description: Loan maturity date
  name: maturityDate
  type: string
- description: Next repayment due date
  name: nextPaymentDate
  type: string
- description: Next repayment amount due
  name: nextPaymentAmount
  type: number
- description: Frequency of loan repayments
  name: repaymentFrequency
  type: string
- description: Loan status
  name: status
  type: string
- description: Amount currently overdue
  name: overdueAmount
  type: number
- description: Number of days past due
  name: daysPastDue
  type: integer
provider_name: Temenos Transact
provider_slug: temenos-transact
schema_file: json-schema/temenos-transact-core-banking-loan-schema.json
slug: temenos-transact-core-banking-loan
tags:
- Banking
- Core Banking
- Digital Banking
- Enterprise
- Financial Services
- Fintech
title: Loan
---
