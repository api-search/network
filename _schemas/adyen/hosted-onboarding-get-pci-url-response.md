---
description: GetPciUrlResponse schema from Adyen API
layout: schema
name: GetPciUrlResponse
properties_list:
- description: Information about any invalid fields.
  name: invalidFields
  type: array
- description: The reference of a request. Can be used to uniquely identify the request.
  name: pspReference
  type: string
- description: The URL to the PCI compliance questionnaire where you should redirect your account holder. This URL must be used within 30 seconds and can only be used once.
  name: redirectUrl
  type: string
- description: The result code.
  name: resultCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/hosted-onboarding-get-pci-url-response-schema.json
slug: hosted-onboarding-get-pci-url-response
tags:
- Payments
- Financial Services
- Fintech
title: GetPciUrlResponse
---
