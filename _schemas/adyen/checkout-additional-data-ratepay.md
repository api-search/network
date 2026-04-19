---
description: AdditionalDataRatepay schema from Adyen API
layout: schema
name: AdditionalDataRatepay
properties_list:
- description: Amount the customer has to pay each month.
  name: ratepay.installmentAmount
  type: string
- description: Interest rate of this installment.
  name: ratepay.interestRate
  type: string
- description: Amount of the last installment.
  name: ratepay.lastInstallmentAmount
  type: string
- description: Calendar day of the first payment.
  name: ratepay.paymentFirstday
  type: string
- description: Date the merchant delivered the goods to the customer.
  name: ratepaydata.deliveryDate
  type: string
- description: Date by which the customer must settle the payment.
  name: ratepaydata.dueDate
  type: string
- description: Invoice date, defined by the merchant. If not included, the invoice date is set to the delivery date.
  name: ratepaydata.invoiceDate
  type: string
- description: Identification name or number for the invoice, defined by the merchant.
  name: ratepaydata.invoiceId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-additional-data-ratepay-schema.json
slug: checkout-additional-data-ratepay
tags:
- Payments
- Financial Services
- Fintech
title: AdditionalDataRatepay
---
