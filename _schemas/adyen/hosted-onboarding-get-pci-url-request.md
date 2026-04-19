---
description: GetPciUrlRequest schema from Adyen API
layout: schema
name: GetPciUrlRequest
properties_list:
- description: The account holder code you provided when you created the account holder.
  name: accountHolderCode
  type: string
- description: The URL where the account holder will be redirected back to after they fill out the questionnaire, or if their session times out. Maximum length of 500 characters.
  name: returnUrl
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/hosted-onboarding-get-pci-url-request-schema.json
slug: hosted-onboarding-get-pci-url-request
tags:
- Payments
- Financial Services
- Fintech
title: GetPciUrlRequest
---
