---
description: OnboardingLinkInfo schema from Adyen API
layout: schema
name: OnboardingLinkInfo
properties_list:
- description: The language that will be used for the page, specified by a combination of two letter [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language and [ISO 3166-1 alpha-2](https://en.wi
  name: locale
  type: string
- description: The URL where the user is redirected after they complete hosted onboarding.
  name: redirectUrl
  type: string
- description: 'Boolean key-value pairs indicating the settings for the hosted onboarding page. The keys are the settings. Possible keys: By default, these values are set to **true**. Set to **false** to not allow th'
  name: settings
  type: object
- description: The unique identifier of the hosted onboarding theme.
  name: themeId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-onboarding-link-info-schema.json
slug: legal-entity-onboarding-link-info
tags:
- Payments
- Financial Services
- Fintech
title: OnboardingLinkInfo
---
