---
description: CreateMerchantWebhookRequest schema from Adyen API
layout: schema
name: CreateMerchantWebhookRequest
properties_list:
- description: 'Indicates if expired SSL certificates are accepted. Default value: **false**.'
  name: acceptsExpiredCertificate
  type: boolean
- description: 'Indicates if self-signed SSL certificates are accepted. Default value: **false**.'
  name: acceptsSelfSignedCertificate
  type: boolean
- description: 'Indicates if untrusted SSL certificates are accepted. Default value: **false**.'
  name: acceptsUntrustedRootCertificate
  type: boolean
- description: Indicates if the webhook configuration is active. The field must be **true** for us to send webhooks about events related an account.
  name: active
  type: boolean
- description: Additional shopper and transaction information to be included in your [standard notifications](https://docs.adyen.com/development-resources/webhooks/understand-notifications#event-codes). Find out mor
  name: additionalSettings
  type: object
- description: 'Format or protocol for receiving webhooks. Possible values: * **soap** * **http** * **json**'
  name: communicationFormat
  type: string
- description: Your description for this webhook configuration.
  name: description
  type: string
- description: 'SSL version to access the public webhook URL specified in the `url` field. Possible values: * **TLSv1.3** * **TLSv1.2** * **HTTP** - Only allowed on Test environment. If not specified, the webhook wil'
  name: encryptionProtocol
  type: string
- description: 'Network type for Terminal API notification webhooks. Possible values: * **public** * **local** Default Value: **public**.'
  name: networkType
  type: string
- description: Password to access the webhook URL.
  name: password
  type: string
- description: 'Indicates if the SOAP action header needs to be populated. Default value: **false**. Only applies if `communicationFormat`: **soap**.'
  name: populateSoapActionHeader
  type: boolean
- description: 'The type of webhook that is being created. Possible values are: - **standard** - **account-settings-notification** - **banktransfer-notification** - **boletobancario-notification** - **directdebit-not'
  name: type
  type: string
- description: Public URL where webhooks will be sent, for example **https://www.domain.com/webhook-endpoint**.
  name: url
  type: string
- description: Username to access the webhook URL.
  name: username
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-create-merchant-webhook-request-schema.json
slug: management-create-merchant-webhook-request
tags:
- Payments
- Financial Services
- Fintech
title: CreateMerchantWebhookRequest
---
