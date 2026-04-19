---
description: ShowPages schema from Adyen API
layout: schema
name: ShowPages
properties_list:
- description: Indicates whether the page with bank account details must be shown. Defaults to **true**.
  name: bankDetailsSummaryPage
  type: boolean
- description: Indicates whether the bank check instant verification' details must be shown. Defaults to **true**.
  name: bankVerificationPage
  type: boolean
- description: Indicates whether the page with the company's or organization's details must be shown. Defaults to **true**.
  name: businessDetailsSummaryPage
  type: boolean
- description: Indicates whether the checks overview page must be shown. Defaults to **false**.
  name: checksOverviewPage
  type: boolean
- description: Indicates whether the page with the individual's details must be shown. Defaults to **true**.
  name: individualDetailsSummaryPage
  type: boolean
- description: Indicates whether the page with the legal arrangements' details must be shown. Defaults to **true**.
  name: legalArrangementsDetailsSummaryPage
  type: boolean
- description: Indicates whether the page to manually add bank account' details must be shown. Defaults to **true**.
  name: manualBankAccountPage
  type: boolean
- description: Indicates whether the page with the shareholders' details must be shown. Defaults to **true**.
  name: shareholderDetailsSummaryPage
  type: boolean
- description: Indicates whether the welcome page must be shown. Defaults to **false**.
  name: welcomePage
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/hosted-onboarding-show-pages-schema.json
slug: hosted-onboarding-show-pages
tags:
- Payments
- Financial Services
- Fintech
title: ShowPages
---
