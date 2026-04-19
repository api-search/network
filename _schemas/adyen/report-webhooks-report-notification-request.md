---
description: ReportNotificationRequest schema from Adyen API
layout: schema
name: ReportNotificationRequest
properties_list:
- description: Contains event details.
  name: data
  type: object
- description: 'The environment from which the webhook originated. Possible values: **test**, **live**.'
  name: environment
  type: string
- description: Type of webhook.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/report-webhooks-report-notification-request-schema.json
slug: report-webhooks-report-notification-request
tags:
- Payments
- Financial Services
- Fintech
title: ReportNotificationRequest
---
