---
description: Request body for adding a joint insured to a policy
layout: schema
name: AddJointInsuredRequest
properties_list:
- description: Legal name of the company to add as joint insured
  name: companyName
  type: string
- description: Company registration number
  name: registrationNumber
  type: string
- description: ISO 3166-1 alpha-2 country code
  name: country
  type: string
provider_name: Allianz Trade
provider_slug: allianz-trade-online
schema_file: json-schema/trade-policy-add_joint_insured_request-schema.json
slug: trade-policy-add_joint_insured_request
tags:
- Credit Insurance
- Insurance
- Risk Management
- Trade Credit
- E-Commerce
- Surety
title: AddJointInsuredRequest
---
