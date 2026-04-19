---
description: TaxReportingClassification schema from Adyen API
layout: schema
name: TaxReportingClassification
properties_list:
- description: 'The organization''s business type. Possible values: **other**, **listedPublicCompany**, **subsidiaryOfListedPublicCompany**, **governmentalOrganization**, **internationalOrganization**, **financialInst'
  name: businessType
  type: string
- description: The Global Intermediary Identification Number (GIIN) required for FATCA. Only required if the organization is a US financial institution and the `businessType` is **financialInstitution**.
  name: financialInstitutionNumber
  type: string
- description: 'The organization''s main source of income. Possible values: **businessOperation**, **realEstateSales**, **investmentInterestOrRoyalty**, **propertyRental**, **other**.'
  name: mainSourceOfIncome
  type: string
- description: 'The tax reporting classification type. Possible values: **nonFinancialNonReportable**, **financialNonReportable**, **nonFinancialActive**, **nonFinancialPassive**.'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-tax-reporting-classification-schema.json
slug: legal-entity-tax-reporting-classification
tags:
- Payments
- Financial Services
- Fintech
title: TaxReportingClassification
---
