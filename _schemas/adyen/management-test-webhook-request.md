---
description: TestWebhookRequest schema from Adyen API
layout: schema
name: TestWebhookRequest
properties_list:
- description: Custom test notification object. Required when the [`types`](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/companies/{companyId}/webhooks/{webhookId}/test__reqParam_types) list conta
  name: notification
  type: object
- description: 'List of event codes for which to send test notifications. Only the webhook types below are supported. Possible values if webhook `type`: **standard**: * **AUTHORISATION** * **CHARGEBACK_REVERSED** * *'
  name: types
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-test-webhook-request-schema.json
slug: management-test-webhook-request
tags:
- Payments
- Financial Services
- Fintech
title: TestWebhookRequest
---
