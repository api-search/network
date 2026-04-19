---
description: Installments schema from Adyen API
layout: schema
name: Installments
properties_list:
- description: The installment plan, used for [card installments in Japan](https://docs.adyen.com/payment-methods/cards/credit-card-installments#make-a-payment-japan). By default, this is set to **regular**. Possibl
  name: plan
  type: string
- description: Defines the number of installments. Its value needs to be greater than zero. Usually, the maximum allowed number of installments is capped. For example, it may not be possible to split a payment in mo
  name: value
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-installments-schema.json
slug: payments-installments
tags:
- Payments
- Financial Services
- Fintech
title: Installments
---
