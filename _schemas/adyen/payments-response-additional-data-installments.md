---
description: ResponseAdditionalDataInstallments schema from Adyen API
layout: schema
name: ResponseAdditionalDataInstallments
properties_list:
- description: Type of installment. The value of `installmentType` should be **IssuerFinanced**.
  name: installmentPaymentData.installmentType
  type: string
- description: Annual interest rate.
  name: installmentPaymentData.option[itemNr].annualPercentageRate
  type: string
- description: First Installment Amount in minor units.
  name: installmentPaymentData.option[itemNr].firstInstallmentAmount
  type: string
- description: Installment fee amount in minor units.
  name: installmentPaymentData.option[itemNr].installmentFee
  type: string
- description: Interest rate for the installment period.
  name: installmentPaymentData.option[itemNr].interestRate
  type: string
- description: Maximum number of installments possible for this payment.
  name: installmentPaymentData.option[itemNr].maximumNumberOfInstallments
  type: string
- description: Minimum number of installments possible for this payment.
  name: installmentPaymentData.option[itemNr].minimumNumberOfInstallments
  type: string
- description: Total number of installments possible for this payment.
  name: installmentPaymentData.option[itemNr].numberOfInstallments
  type: string
- description: Subsequent Installment Amount in minor units.
  name: installmentPaymentData.option[itemNr].subsequentInstallmentAmount
  type: string
- description: Total amount in minor units.
  name: installmentPaymentData.option[itemNr].totalAmountDue
  type: string
- description: 'Possible values: * PayInInstallmentsOnly * PayInFullOnly * PayInFullOrInstallments'
  name: installmentPaymentData.paymentOptions
  type: string
- description: 'The number of installments that the payment amount should be charged with. Example: 5 > Only relevant for card payments in countries that support installments.'
  name: installments.value
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-response-additional-data-installments-schema.json
slug: payments-response-additional-data-installments
tags:
- Payments
- Financial Services
- Fintech
title: ResponseAdditionalDataInstallments
---
