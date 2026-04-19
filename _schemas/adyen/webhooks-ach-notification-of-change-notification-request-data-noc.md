---
description: AchNotificationOfChangeNotificationRequestDataNoc schema from Adyen API
layout: schema
name: AchNotificationOfChangeNotificationRequestDataNoc
properties_list:
- description: New bank account number.
  name: newBankAccountNumber
  type: string
- description: 'New bank account type. Possible values: * **Savings** * **Checking**'
  name: newBankAccountType
  type: string
- description: New branch code.
  name: newBranchCode
  type: string
- description: 'Notification of Change reason code. Possible values: * **C01** : Incorrect bank account number. * **C02** : Incorrect transit/routing number. * **C03** : Incorrect transit/routing number and bank acco'
  name: reasonCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/webhooks-ach-notification-of-change-notification-request-data-noc-schema.json
slug: webhooks-ach-notification-of-change-notification-request-data-noc
tags:
- Payments
- Financial Services
- Fintech
title: AchNotificationOfChangeNotificationRequestDataNoc
---
