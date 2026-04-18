---
description: ''
layout: schema
name: PrimaryEmail
properties_list:
- description: Count of days since the email was first observed in Ekata's Identity Network. If the email has not been observed before, first_seen_days will be 0.
  name: firstSeenDays
  type: integer
- description: Number of days that have passed since the email address was last seen.
  name: lastSeenDays
  type: integer
- description: True if the email address is valid
  name: valid
  type: boolean
- description: The date when the email domain was created. Format is YYYY-MM-DD.
  name: domainCreationDate
  type: string
- description: The match status between the input name and the queried entity.
  name: matchToName
  type: string
- description: Number of times email has been seen in last 180 days.
  name: mailboxVelocity
  type: integer
- description: True if the email domain is disposable. Disposable emails are generally associated with fraudulent activities. If true, this is one of the strongest risk indicators and the transaction should be flagg
  name: isDisposable
  type: boolean
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-identity-insights-for-transactions-primary-email-schema.json
slug: mastercard-identity-insights-for-transactions-primary-email
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: PrimaryEmail
---
