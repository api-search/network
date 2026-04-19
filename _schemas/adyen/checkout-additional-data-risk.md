---
description: AdditionalDataRisk schema from Adyen API
layout: schema
name: AdditionalDataRisk
properties_list:
- description: The data for your custom risk field. For more information, refer to [Create custom risk fields](https://docs.adyen.com/risk-management/configure-custom-risk-rules#step-1-create-custom-risk-fields).
  name: riskdata.[customFieldName]
  type: string
- description: The price of item in the basket, represented in [minor units](https://docs.adyen.com/development-resources/currency-codes).
  name: riskdata.basket.item[itemNr].amountPerItem
  type: string
- description: Brand of the item.
  name: riskdata.basket.item[itemNr].brand
  type: string
- description: Category of the item.
  name: riskdata.basket.item[itemNr].category
  type: string
- description: Color of the item.
  name: riskdata.basket.item[itemNr].color
  type: string
- description: The three-character [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217).
  name: riskdata.basket.item[itemNr].currency
  type: string
- description: ID of the item.
  name: riskdata.basket.item[itemNr].itemID
  type: string
- description: Manufacturer of the item.
  name: riskdata.basket.item[itemNr].manufacturer
  type: string
- description: A text description of the product the invoice line refers to.
  name: riskdata.basket.item[itemNr].productTitle
  type: string
- description: Quantity of the item purchased.
  name: riskdata.basket.item[itemNr].quantity
  type: string
- description: Email associated with the given product in the basket (usually in electronic gift cards).
  name: riskdata.basket.item[itemNr].receiverEmail
  type: string
- description: Size of the item.
  name: riskdata.basket.item[itemNr].size
  type: string
- description: '[Stock keeping unit](https://en.wikipedia.org/wiki/Stock_keeping_unit).'
  name: riskdata.basket.item[itemNr].sku
  type: string
- description: '[Universal Product Code](https://en.wikipedia.org/wiki/Universal_Product_Code).'
  name: riskdata.basket.item[itemNr].upc
  type: string
- description: Code of the promotion.
  name: riskdata.promotions.promotion[itemNr].promotionCode
  type: string
- description: The discount amount of the promotion, represented in [minor units](https://docs.adyen.com/development-resources/currency-codes).
  name: riskdata.promotions.promotion[itemNr].promotionDiscountAmount
  type: string
- description: The three-character [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217).
  name: riskdata.promotions.promotion[itemNr].promotionDiscountCurrency
  type: string
- description: Promotion's percentage discount. It is represented in percentage value and there is no need to include the '%' sign. e.g. for a promotion discount of 30%, the value of the field should be 30.
  name: riskdata.promotions.promotion[itemNr].promotionDiscountPercentage
  type: string
- description: Name of the promotion.
  name: riskdata.promotions.promotion[itemNr].promotionName
  type: string
- description: Reference number of the risk profile that you want to apply to the payment. If not provided or left blank, the merchant-level account's default risk profile will be applied to the payment. For more in
  name: riskdata.riskProfileReference
  type: string
- description: If this parameter is provided with the value **true**, risk checks for the payment request are skipped and the transaction will not get a risk score.
  name: riskdata.skipRisk
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-additional-data-risk-schema.json
slug: checkout-additional-data-risk
tags:
- Payments
- Financial Services
- Fintech
title: AdditionalDataRisk
---
