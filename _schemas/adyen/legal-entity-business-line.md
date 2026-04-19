---
description: BusinessLine schema from Adyen API
layout: schema
name: BusinessLine
properties_list:
- description: 'The capability for which you are creating the business line. Possible values: **receivePayments**, **receiveFromPlatformPayments**, **issueBankAccount**'
  name: capability
  type: string
- description: The unique identifier of the business line.
  name: id
  type: string
- description: 'A code that represents the [industry of the legal entity](https://docs.adyen.com/marketplaces-and-platforms/verification-requirements/reference-additional-products/#list-industry-codes). For example, '
  name: industryCode
  type: string
- description: Unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities__resParam_id) that owns the business line.
  name: legalEntityId
  type: string
- description: The verification errors related to capabilities for this supporting entity.
  name: problems
  type: array
- description: 'A list of channels where goods or services are sold. Possible values: **pos**, **posMoto**, **eCommerce**, **ecomMoto**, **payByLink**. Required only in combination with the `service` **paymentProcess'
  name: salesChannels
  type: array
- description: 'The service for which you are creating the business line. Possible values: * **paymentProcessing** * **banking**'
  name: service
  type: string
- description: Contains information about the source of your user's funds. Required only for the `service` **banking**.
  name: sourceOfFunds
  type: object
- description: List of website URLs where your user's goods or services are sold. When this is required for a service but your user does not have an online presence, provide the reason in the `webDataExemption` obje
  name: webData
  type: array
- description: The reason why the web data is not provided.
  name: webDataExemption
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/legal-entity-business-line-schema.json
slug: legal-entity-business-line
tags:
- Payments
- Financial Services
- Fintech
title: BusinessLine
---
