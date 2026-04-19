---
description: GetOnboardingUrlResponse schema from Adyen API
layout: schema
name: GetOnboardingUrlResponse
properties_list:
- description: Information about any invalid fields.
  name: invalidFields
  type: array
- description: The reference of a request. Can be used to uniquely identify the request.
  name: pspReference
  type: string
- description: The URL to the Hosted Onboarding Page where you should redirect your sub-merchant. This URL must be used within 30 seconds and can only be used once.
  name: redirectUrl
  type: string
- description: The result code.
  name: resultCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/hosted-onboarding-get-onboarding-url-response-schema.json
slug: hosted-onboarding-get-onboarding-url-response
tags:
- Payments
- Financial Services
- Fintech
title: GetOnboardingUrlResponse
---
