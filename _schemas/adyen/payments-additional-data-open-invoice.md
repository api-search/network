---
description: AdditionalDataOpenInvoice schema from Adyen API
layout: schema
name: AdditionalDataOpenInvoice
properties_list:
- description: Holds different merchant data points like product, purchase, customer, and so on. It takes data in a Base64 encoded string. The `merchantData` parameter needs to be added to the `openinvoicedata` sign
  name: openinvoicedata.merchantData
  type: string
- description: The number of invoice lines included in `openinvoicedata`. There needs to be at least one line, so `numberOfLines` needs to be at least 1.
  name: openinvoicedata.numberOfLines
  type: string
- description: First name of the recipient. If the delivery address and the billing address are different, specify the `recipientFirstName` and `recipientLastName` to share the delivery address with Klarna. Otherwis
  name: openinvoicedata.recipientFirstName
  type: string
- description: Last name of the recipient. If the delivery address and the billing address are different, specify the `recipientFirstName` and `recipientLastName` to share the delivery address with Klarna. Otherwise
  name: openinvoicedata.recipientLastName
  type: string
- description: The three-character ISO currency code.
  name: openinvoicedataLine[itemNr].currencyCode
  type: string
- description: A text description of the product the invoice line refers to.
  name: openinvoicedataLine[itemNr].description
  type: string
- description: The price for one item in the invoice line, represented in minor units. The due amount for the item, VAT excluded.
  name: openinvoicedataLine[itemNr].itemAmount
  type: string
- description: A unique id for this item. Required for RatePay if the description of each item is not unique.
  name: openinvoicedataLine[itemNr].itemId
  type: string
- description: The VAT due for one item in the invoice line, represented in minor units.
  name: openinvoicedataLine[itemNr].itemVatAmount
  type: string
- description: The VAT percentage for one item in the invoice line, represented in minor units. For example, 19% VAT is specified as 1900.
  name: openinvoicedataLine[itemNr].itemVatPercentage
  type: string
- description: The number of units purchased of a specific product.
  name: openinvoicedataLine[itemNr].numberOfItems
  type: string
- description: Name of the shipping company handling the the return shipment.
  name: openinvoicedataLine[itemNr].returnShippingCompany
  type: string
- description: The tracking number for the return of the shipment.
  name: openinvoicedataLine[itemNr].returnTrackingNumber
  type: string
- description: URI where the customer can track the return of their shipment.
  name: openinvoicedataLine[itemNr].returnTrackingUri
  type: string
- description: Name of the shipping company handling the delivery.
  name: openinvoicedataLine[itemNr].shippingCompany
  type: string
- description: Shipping method.
  name: openinvoicedataLine[itemNr].shippingMethod
  type: string
- description: The tracking number for the shipment.
  name: openinvoicedataLine[itemNr].trackingNumber
  type: string
- description: URI where the customer can track their shipment.
  name: openinvoicedataLine[itemNr].trackingUri
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-additional-data-open-invoice-schema.json
slug: payments-additional-data-open-invoice
tags:
- Payments
- Financial Services
- Fintech
title: AdditionalDataOpenInvoice
---
