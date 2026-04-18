---
description: 'An indicator to help explain the status of the account being inquired on. Possible values are: * `VALID` = Matches the account as reported by the issuer. * `UNKNOWN` = Account number is not known to ABU or part of a participating BIN (Bank Identification Number) and/or issuer. * `NON_PARTICIPATING` = Account number is not known to ABU or part of a non-participating BIN (Bank Identification Number) and/or issuer. * `CONTACT` (C) = Contact the issuer. * `EXPIRY` (E) = The card inquired on is expired, updated expiry date returned. * `ACCOUNT_UPDATE` (A) = The card inquired on is updated, updated card number and expiry date returned.'
layout: schema
name: ResponseIndicator
properties_list: []
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-automatic-billing-updater-response-indicator-schema.json
slug: mastercard-automatic-billing-updater-response-indicator
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: ResponseIndicator
---
