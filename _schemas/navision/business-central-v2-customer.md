---
description: ''
layout: schema
name: Customer
properties_list:
- description: ETag for concurrency control
  name: '@odata.etag'
  type: string
- description: The unique identifier of the customer
  name: id
  type: string
- description: The customer number
  name: number
  type: string
- description: The customer display name
  name: displayName
  type: string
- description: The customer type
  name: type
  type: string
- description: First line of the address
  name: addressLine1
  type: string
- description: Second line of the address
  name: addressLine2
  type: string
- description: The city
  name: city
  type: string
- description: The state or province code
  name: state
  type: string
- description: The country/region code
  name: country
  type: string
- description: The postal code
  name: postalCode
  type: string
- description: The phone number
  name: phoneNumber
  type: string
- description: The email address
  name: email
  type: string
- description: The website URL
  name: website
  type: string
- description: The salesperson code
  name: salespersonCode
  type: string
- description: The balance due from the customer
  name: balanceDue
  type: number
- description: The credit limit
  name: creditLimit
  type: number
- description: Whether the customer is tax liable
  name: taxLiable
  type: boolean
- description: The tax area ID
  name: taxAreaId
  type: string
- description: The tax area display name
  name: taxAreaDisplayName
  type: string
- description: The tax registration number
  name: taxRegistrationNumber
  type: string
- description: The currency ID
  name: currencyId
  type: string
- description: The currency code
  name: currencyCode
  type: string
- description: The payment terms ID
  name: paymentTermsId
  type: string
- description: The shipment method ID
  name: shipmentMethodId
  type: string
- description: The payment method ID
  name: paymentMethodId
  type: string
- description: Whether the customer is blocked
  name: blocked
  type: string
- description: The date and time when the customer was last modified
  name: lastModifiedDateTime
  type: string
provider_name: Microsoft Dynamics NAV
provider_slug: navision
schema_file: json-schema/business-central-v2-customer-schema.json
slug: business-central-v2-customer
tags:
- Business Management
- Dynamics NAV
- ERP
- Finance
- Inventory
- Microsoft
- Navision
title: Customer
---
