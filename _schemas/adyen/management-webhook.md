---
description: Webhook schema from Adyen API
layout: schema
name: Webhook
properties_list:
- description: References to resources connected with this webhook.
  name: _links
  type: object
- description: 'Indicates if expired SSL certificates are accepted. Default value: **false**.'
  name: acceptsExpiredCertificate
  type: boolean
- description: 'Indicates if self-signed SSL certificates are accepted. Default value: **false**.'
  name: acceptsSelfSignedCertificate
  type: boolean
- description: 'Indicates if untrusted SSL certificates are accepted. Default value: **false**.'
  name: acceptsUntrustedRootCertificate
  type: boolean
- description: Reference to the account the webook is set on.
  name: accountReference
  type: string
- description: Indicates if the webhook configuration is active. The field must be **true** for you to receive webhooks about events related an account.
  name: active
  type: boolean
- description: Additional shopper and transaction information to be included in your [standard notifications](https://docs.adyen.com/development-resources/webhooks/understand-notifications#event-codes). Find out mor
  name: additionalSettings
  type: object
- description: The alias of our SSL certificate. When you receive a notification from us, the alias from the HMAC signature will match this alias.
  name: certificateAlias
  type: string
- description: 'Format or protocol for receiving webhooks. Possible values: * **soap** * **http** * **json**'
  name: communicationFormat
  type: string
- description: Your description for this webhook configuration.
  name: description
  type: string
- description: 'SSL version to access the public webhook URL specified in the `url` field. Possible values: * **TLSv1.3** * **TLSv1.2** * **HTTP** - Only allowed on Test environment. If not specified, the webhook wil'
  name: encryptionProtocol
  type: string
- description: 'Shows how merchant accounts are included in company-level webhooks. Possible values: * **includeAccounts** * **excludeAccounts** * **allAccounts**: Includes all merchant accounts, and does not require'
  name: filterMerchantAccountType
  type: string
- description: A list of merchant account names that are included or excluded from receiving the webhook. Inclusion or exclusion is based on the value defined for `filterMerchantAccountType`. Required if `filterMerc
  name: filterMerchantAccounts
  type: array
- description: Indicates if the webhook configuration has errors that need troubleshooting. If the value is **true**, troubleshoot the configuration using the [testing endpoint](https://docs.adyen.com/api-explorer/#
  name: hasError
  type: boolean
- description: Indicates if the webhook is password protected.
  name: hasPassword
  type: boolean
- description: The [checksum](https://en.wikipedia.org/wiki/Key_checksum_value) of the HMAC key generated for this webhook. You can use this value to uniquely identify the HMAC key configured for this webhook.
  name: hmacKeyCheckValue
  type: string
- description: Unique identifier for this webhook.
  name: id
  type: string
- description: Network type for Terminal API details webhooks.
  name: networkType
  type: string
- description: 'Indicates if the SOAP action header needs to be populated. Default value: **false**. Only applies if `communicationFormat`: **soap**.'
  name: populateSoapActionHeader
  type: boolean
- description: 'The type of webhook. Possible values are: - **standard** - **account-settings-notification** - **banktransfer-notification** - **boletobancario-notification** - **directdebit-notification** - **ach-no'
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
schema_file: json-schema/management-webhook-schema.json
slug: management-webhook
tags:
- Payments
- Financial Services
- Fintech
title: Webhook
---
