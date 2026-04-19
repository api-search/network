---
description: SetupBeneficiaryRequest schema from Adyen API
layout: schema
name: SetupBeneficiaryRequest
properties_list:
- description: The destination account code.
  name: destinationAccountCode
  type: string
- description: A value that can be supplied at the discretion of the executing user.
  name: merchantReference
  type: string
- description: The benefactor account.
  name: sourceAccountCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-setup-beneficiary-request-schema.json
slug: funds-setup-beneficiary-request
tags:
- Payments
- Financial Services
- Fintech
title: SetupBeneficiaryRequest
---
