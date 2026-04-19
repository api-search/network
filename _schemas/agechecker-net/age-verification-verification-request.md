---
description: VerificationRequest schema from AgeChecker.Net API
layout: schema
name: VerificationRequest
properties_list:
- description: Customer first name.
  name: first_name
  type: string
- description: Customer last name.
  name: last_name
  type: string
- description: Customer date of birth (YYYY-MM-DD).
  name: birth_date
  type: string
- description: Street address.
  name: address
  type: string
- description: City.
  name: city
  type: string
- description: State or province code.
  name: state
  type: string
- description: Postal/ZIP code.
  name: zip
  type: string
- description: ISO 3166-1 alpha-2 country code.
  name: country
  type: string
- description: Customer email address.
  name: email
  type: string
- description: Customer phone number.
  name: phone
  type: string
- description: Customer's IP address.
  name: ip_address
  type: string
- description: Minimum age required (default is 21 for alcohol, 18 for tobacco).
  name: minimum_age
  type: integer
provider_name: AgeChecker.Net
provider_slug: agechecker-net
schema_file: json-schema/age-verification-verification-request-schema.json
slug: age-verification-verification-request
tags:
- Age Verification
- Identity
- Compliance
- Regulatory
- E-Commerce
title: VerificationRequest
---
