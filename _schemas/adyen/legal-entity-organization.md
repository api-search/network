---
description: Organization schema from Adyen API
layout: schema
name: Organization
properties_list:
- description: The date when the organization was incorporated in YYYY-MM-DD format.
  name: dateOfIncorporation
  type: string
- description: Your description for the organization.
  name: description
  type: string
- description: The organization's trading name, if different from the registered legal name.
  name: doingBusinessAs
  type: string
- description: The email address of the legal entity.
  name: email
  type: string
- description: The organization's legal name.
  name: legalName
  type: string
- description: The phone number of the legal entity.
  name: phone
  type: object
- description: The address where the organization operates from. Provide this if the principal place of business is different from the `registeredAddress`.
  name: principalPlaceOfBusiness
  type: object
- description: The address of the organization registered at their registrar (such as the Chamber of Commerce).
  name: registeredAddress
  type: object
- description: The organization's registration number.
  name: registrationNumber
  type: string
- description: Information about the organization's publicly traded stock. Provide this object only if `type` is **listedPublicCompany**.
  name: stockData
  type: object
- description: The tax information of the organization.
  name: taxInformation
  type: array
- description: The tax reporting classification (FATCA/CRS self-certification) of the organization.
  name: taxReportingClassification
  type: object
- description: 'Type of organization. Possible values: **associationIncorporated**, **governmentalOrganization**, **listedPublicCompany**, **nonProfit**, **partnershipIncorporated**, **privateCompany**.'
  name: type
  type: string
- description: 'The reason the organization has not provided a VAT number. Possible values: **industryExemption**, **belowTaxThreshold**.'
  name: vatAbsenceReason
  type: string
- description: The organization's VAT number.
  name: vatNumber
  type: string
- description: The website and app URL of the legal entity.
  name: webData
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-organization-schema.json
slug: legal-entity-organization
tags:
- Payments
- Financial Services
- Fintech
title: Organization
---
