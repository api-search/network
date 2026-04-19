---
description: BeneficiarySetupNotificationContent schema from Adyen API
layout: schema
name: BeneficiarySetupNotificationContent
properties_list:
- description: The code of the beneficiary account.
  name: destinationAccountCode
  type: string
- description: The code of the beneficiary Account Holder.
  name: destinationAccountHolderCode
  type: string
- description: A listing of the invalid fields which have caused the Setup Beneficiary request to fail. If this is empty, the Setup Beneficiary request has succeeded.
  name: invalidFields
  type: array
- description: The reference provided by the merchant.
  name: merchantReference
  type: string
- description: The code of the benefactor account.
  name: sourceAccountCode
  type: string
- description: The code of the benefactor Account Holder.
  name: sourceAccountHolderCode
  type: string
- description: The date on which the beneficiary was set up and funds transferred from benefactor to beneficiary.
  name: transferDate
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-beneficiary-setup-notification-content-schema.json
slug: notifications-beneficiary-setup-notification-content
tags:
- Payments
- Financial Services
- Fintech
title: BeneficiarySetupNotificationContent
---
