---
description: A joint insured entity registered under a policy
layout: schema
name: JointInsured
properties_list:
- description: Unique identifier for the joint insured
  name: jointInsuredId
  type: string
- description: Parent policy identifier
  name: policyId
  type: string
- description: Legal name of the joint insured company
  name: companyName
  type: string
- description: Company registration number
  name: registrationNumber
  type: string
- description: ISO 3166-1 alpha-2 country code
  name: country
  type: string
- description: Current status of the joint insured
  name: status
  type: string
provider_name: Allianz Trade
provider_slug: allianz-trade-online
schema_file: json-schema/trade-policy-joint_insured-schema.json
slug: trade-policy-joint_insured
tags:
- Credit Insurance
- Insurance
- Risk Management
- Trade Credit
- E-Commerce
- Surety
title: JointInsured
---
