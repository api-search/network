---
description: CollectInformation schema from Adyen API
layout: schema
name: CollectInformation
properties_list:
- description: Indicates whether [bank account details](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-checks/bank-account-check) must be collected. Default is **true**.
  name: bankDetails
  type: boolean
- description: Indicates whether [business details](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-checks/company-check) must be collected. Default is **true**.
  name: businessDetails
  type: boolean
- description: Indicates whether [individual details](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-checks/identity-check) must be collected. Default is **true**.
  name: individualDetails
  type: boolean
- description: Indicates whether [legal arrangement details](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-checks/legal-arrangements) must be collected. Default is **true**.
  name: legalArrangementDetails
  type: boolean
- description: Indicates whether answers to a [PCI questionnaire](https://docs.adyen.com/marketplaces-and-platforms/classic/platforms-for-partners#onboard-partner-platform) must be collected. Applies only to partner
  name: pciQuestionnaire
  type: boolean
- description: Indicates whether [shareholder details](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-checks/identity-check) must be collected. Defaults to **true**.
  name: shareholderDetails
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/hosted-onboarding-collect-information-schema.json
slug: hosted-onboarding-collect-information
tags:
- Payments
- Financial Services
- Fintech
title: CollectInformation
---
