---
description: Represents a vendor (supplier) entity in Dynamics 365 Business Central. Vendors are the parties from whom the company purchases goods or services. Each vendor record contains contact information, financial settings, and payment terms.
layout: schema
name: Vendor
properties_list:
- description: ETag for optimistic concurrency control
  name: '@odata.etag'
  type: string
- description: The unique identifier (GUID) of the vendor record
  name: id
  type: string
- description: The vendor number, a unique business identifier assigned automatically or manually
  name: number
  type: string
- description: The display name of the vendor
  name: displayName
  type: string
- description: The first line of the vendor's street address
  name: addressLine1
  type: string
- description: The second line of the vendor's street address
  name: addressLine2
  type: string
- description: The city of the vendor's address
  name: city
  type: string
- description: The state or province code of the vendor's address
  name: state
  type: string
- description: The country/region code of the vendor's address
  name: country
  type: string
- description: The postal or ZIP code of the vendor's address
  name: postalCode
  type: string
- description: The vendor's primary phone number
  name: phoneNumber
  type: string
- description: The vendor's email address
  name: email
  type: string
- description: The vendor's website URL
  name: website
  type: string
- description: The vendor's tax registration number (VAT number or similar)
  name: taxRegistrationNumber
  type: string
- description: The unique identifier of the currency used for this vendor
  name: currencyId
  type: string
- description: The currency code (e.g., USD, EUR) used for transactions with this vendor
  name: currencyCode
  type: string
- description: The unique identifier of the payment terms assigned to the vendor
  name: paymentTermsId
  type: string
- description: The unique identifier of the payment method used for the vendor
  name: paymentMethodId
  type: string
- description: Indicates whether the vendor is liable for sales tax
  name: taxLiable
  type: boolean
- description: 'Specifies which transactions are blocked for the vendor: blank (none), Payment, or All'
  name: blocked
  type: string
- description: The current balance owed to the vendor (read-only, computed)
  name: balance
  type: number
- description: The date and time the vendor record was last modified (read-only)
  name: lastModifiedDateTime
  type: string
provider_name: Microsoft Dynamics NAV
provider_slug: navision
schema_file: json-schema/vendor.json
slug: vendor
tags:
- Business Management
- Dynamics NAV
- ERP
- Finance
- Inventory
- Microsoft
- Navision
title: Vendor
---
