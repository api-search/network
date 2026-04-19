---
description: GetOnboardingUrlRequest schema from Adyen API
layout: schema
name: GetOnboardingUrlRequest
properties_list:
- description: The account holder code you provided when you created the account holder.
  name: accountHolderCode
  type: string
- description: Contains indicators whether the page should only collect information for specific [KYC checks](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-checks). By default, the page coll
  name: collectInformation
  type: object
- description: Indicates if editing checks is allowed even if all the checks have passed.
  name: editMode
  type: boolean
- description: The URL to which the account holder is redirected after completing an OAuth authentication with a bank through Trustly/PayMyBank.
  name: mobileOAuthCallbackUrl
  type: string
- description: The platform name which will show up in the welcome page.
  name: platformName
  type: string
- description: 'The URL where the account holder will be redirected back to after they complete the onboarding, or if their session times out. Maximum length of 500 characters. If you don''t provide this, the account '
  name: returnUrl
  type: string
- description: The language to be used in the page, specified by a combination of a language and country code. For example, **pt-BR**. If not specified in the request or if the language is not supported, the page us
  name: shopperLocale
  type: string
- description: Contains indicators whether specific pages must be shown to the account holder.
  name: showPages
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/hosted-onboarding-get-onboarding-url-request-schema.json
slug: hosted-onboarding-get-onboarding-url-request
tags:
- Payments
- Financial Services
- Fintech
title: GetOnboardingUrlRequest
---
