---
description: The request object for enrolling a new user to Carbon Calculator Experience API.
layout: schema
name: UserProfile
properties_list:
- description: Name of the card-holder. (format- First Name Last Name)
  name: cardholderName
  type: string
- description: User locale which is registered with Issuer.
  name: locale
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-carbon-calculator-experience-user-profile-schema.json
slug: mastercard-carbon-calculator-experience-user-profile
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: UserProfile
---
