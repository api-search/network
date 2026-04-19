---
description: ReportNotificationData schema from Adyen API
layout: schema
name: ReportNotificationData
properties_list:
- description: The account holder related to the report.
  name: accountHolder
  type: object
- description: The balance account related to the report.
  name: balanceAccount
  type: object
- description: The unique identifier of the balance platform.
  name: balancePlatform
  type: string
- description: The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**.
  name: creationDate
  type: string
- description: The URL at which you can download the report. To download, you must authenticate your GET request with your [API credentials](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/overview).
  name: downloadUrl
  type: string
- description: The filename of the report.
  name: fileName
  type: string
- description: Type of report.
  name: reportType
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/report-webhooks-report-notification-data-schema.json
slug: report-webhooks-report-notification-data
tags:
- Payments
- Financial Services
- Fintech
title: ReportNotificationData
---
