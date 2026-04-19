---
description: UltimateParentCompany schema from Adyen API
layout: schema
name: UltimateParentCompany
properties_list:
- description: Address of the ultimate parent company.
  name: address
  type: object
- description: Details about the ultimate parent company's business.
  name: businessDetails
  type: object
- description: Adyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create an ultimate parent company. Required when updating an existing entry in an `/updateAccount
  name: ultimateParentCompanyCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-ultimate-parent-company-schema.json
slug: accounts-ultimate-parent-company
tags:
- Payments
- Financial Services
- Fintech
title: UltimateParentCompany
---
