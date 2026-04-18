---
description: Set of Personally Identifiable Information (PII) associated with a given client.
layout: schema
name: Profile
properties_list:
- description: Maiden name of the client. <br/> This field is required if configured as **Business Mandatory**<font color='red'>* </font>.
  name: maidenName
  type: string
- description: 'Date of birth. <br/> **Conditional Mandatory**<font color=''red''>* </font> field - Required while creating new client. <br/> Date format must be ISO 8601: `YYYY-MM-DD` <br/> where: <br/> YYYY = four-di'
  name: birthDate
  type: string
- description: Birth city of the client. City will be verified against the 'city master setup'. <br/> This field is required if configured as **Business Mandatory**<font color='red'>* </font>.
  name: birthCity
  type: string
- description: Expressed as a 2-letter (Alpha-2) country code as defined in ISO 3166. <br/> For example - IN, US, CA, GB <br/> This field is required if configured as **Business Mandatory**<font color='red'>* </font
  name: birthCountry
  type: string
- description: The status of belonging to a particular nation. <br/> **Conditional Mandatory**<font color='red'>* </font> field - Required while creating new client. <br/> Expressed as a 2-letter (Alpha-2) country c
  name: nationality
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-card-issuance-profile-schema.json
slug: mastercard-card-issuance-profile
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Profile
---
