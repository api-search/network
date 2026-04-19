---
description: AccountInfo schema from Adyen API
layout: schema
name: AccountInfo
properties_list:
- description: 'Indicator for the length of time since this shopper account was created in the merchant''s environment. Allowed values: * notApplicable * thisTransaction * lessThan30Days * from30To60Days * moreThan60D'
  name: accountAgeIndicator
  type: string
- description: Date when the shopper's account was last changed.
  name: accountChangeDate
  type: string
- description: 'Indicator for the length of time since the shopper''s account was last updated. Allowed values: * thisTransaction * lessThan30Days * from30To60Days * moreThan60Days'
  name: accountChangeIndicator
  type: string
- description: Date when the shopper's account was created.
  name: accountCreationDate
  type: string
- description: 'Indicates the type of account. For example, for a multi-account card product. Allowed values: * notApplicable * credit * debit'
  name: accountType
  type: string
- description: Number of attempts the shopper tried to add a card to their account in the last day.
  name: addCardAttemptsDay
  type: integer
- description: Date the selected delivery address was first used.
  name: deliveryAddressUsageDate
  type: string
- description: 'Indicator for the length of time since this delivery address was first used. Allowed values: * thisTransaction * lessThan30Days * from30To60Days * moreThan60Days'
  name: deliveryAddressUsageIndicator
  type: string
- description: Shopper's home phone number (including the country code).
  name: homePhone
  type: string
- description: Shopper's mobile phone number (including the country code).
  name: mobilePhone
  type: string
- description: Date when the shopper last changed their password.
  name: passwordChangeDate
  type: string
- description: 'Indicator when the shopper has changed their password. Allowed values: * notApplicable * thisTransaction * lessThan30Days * from30To60Days * moreThan60Days'
  name: passwordChangeIndicator
  type: string
- description: Number of all transactions (successful and abandoned) from this shopper in the past 24 hours.
  name: pastTransactionsDay
  type: integer
- description: Number of all transactions (successful and abandoned) from this shopper in the past year.
  name: pastTransactionsYear
  type: integer
- description: Date this payment method was added to the shopper's account.
  name: paymentAccountAge
  type: string
- description: 'Indicator for the length of time since this payment method was added to this shopper''s account. Allowed values: * notApplicable * thisTransaction * lessThan30Days * from30To60Days * moreThan60Days'
  name: paymentAccountIndicator
  type: string
- description: Number of successful purchases in the last six months.
  name: purchasesLast6Months
  type: integer
- description: Whether suspicious activity was recorded on this account.
  name: suspiciousActivity
  type: boolean
- description: Shopper's work phone number (including the country code).
  name: workPhone
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payments-account-info-schema.json
slug: payments-account-info
tags:
- Payments
- Financial Services
- Fintech
title: AccountInfo
---
