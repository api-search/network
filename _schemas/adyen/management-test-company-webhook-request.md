---
description: TestCompanyWebhookRequest schema from Adyen API
layout: schema
name: TestCompanyWebhookRequest
properties_list:
- description: List of `merchantId` values for which test webhooks will be sent. The list can have a maximum of 20 `merchantId` values. If not specified, we send sample notifications to all the merchant accounts tha
  name: merchantIds
  type: array
- description: Custom test notification object. Required when the [`types`](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/companies/{companyId}/webhooks/{webhookId}/test__reqParam_types) list conta
  name: notification
  type: object
- description: 'List of event codes for which to send test notifications. Only the webhook types below are supported. Possible values if webhook `type`: **standard**: * **AUTHORISATION** * **CHARGEBACK_REVERSED** * *'
  name: types
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-test-company-webhook-request-schema.json
slug: management-test-company-webhook-request
tags:
- Payments
- Financial Services
- Fintech
title: TestCompanyWebhookRequest
---
