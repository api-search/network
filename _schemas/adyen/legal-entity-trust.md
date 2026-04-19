---
description: Trust schema from Adyen API
layout: schema
name: Trust
properties_list:
- description: The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the governing country.
  name: countryOfGoverningLaw
  type: string
- description: The date when the legal arrangement was incorporated in YYYY-MM-DD format.
  name: dateOfIncorporation
  type: string
- description: Short description about the trust.
  name: description
  type: string
- description: The registered name, if different from the `name`.
  name: doingBusinessAs
  type: string
- description: The legal name.
  name: name
  type: string
- description: The business address. Required if the principal place of business is different from the `registeredAddress`.
  name: principalPlaceOfBusiness
  type: object
- description: The address registered at the registrar, such as the Chamber of Commerce.
  name: registeredAddress
  type: object
- description: The registration number.
  name: registrationNumber
  type: string
- description: The tax information of the entity.
  name: taxInformation
  type: array
- description: 'Type of trust. Possible values for Australian trusts: **cashManagementTrust**, **corporateUnitTrust**, **deceasedEstate**, **discretionaryInvestmentTrust**, **discretionaryServicesManagementTrust**, *'
  name: type
  type: string
- description: The undefined beneficiary information of the entity.
  name: undefinedBeneficiaryInfo
  type: array
- description: 'The reason for not providing a VAT number. Possible values: **industryExemption**, **belowTaxThreshold**.'
  name: vatAbsenceReason
  type: string
- description: The VAT number.
  name: vatNumber
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-trust-schema.json
slug: legal-entity-trust
tags:
- Payments
- Financial Services
- Fintech
title: Trust
---
