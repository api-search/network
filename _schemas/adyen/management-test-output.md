---
description: TestOutput schema from Adyen API
layout: schema
name: TestOutput
properties_list:
- description: Unique identifier of the merchant account that the notification is about.
  name: merchantId
  type: string
- description: 'The response your server returned for the test webhook. Your server must respond with **[accepted]** for the test webhook to be successful (`data.status`: **success**). Find out more about [accepting '
  name: output
  type: string
- description: The [body of the notification webhook](https://docs.adyen.com/development-resources/webhooks/understand-notifications#notification-structure) that was sent to your server.
  name: requestSent
  type: string
- description: The HTTP response code for your server's response to the test webhook. You can use the value of this field together with the the [`output`](https://docs.adyen.com/api-explorer/#/ManagementService/v1/p
  name: responseCode
  type: string
- description: The time between sending the test webhook and receiving the response from your server. You can use it as an indication of how long your server takes to process a webhook notification. Measured in mill
  name: responseTime
  type: string
- description: 'The status of the test request. Possible values are: * **success**, if `data.output`: **[accepted]** and `data.responseCode`: **200**. * **failed**, in all other cases. You can use the value of the [`'
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-test-output-schema.json
slug: management-test-output
tags:
- Payments
- Financial Services
- Fintech
title: TestOutput
---
