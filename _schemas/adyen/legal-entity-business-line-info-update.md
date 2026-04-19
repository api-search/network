---
description: BusinessLineInfoUpdate schema from Adyen API
layout: schema
name: BusinessLineInfoUpdate
properties_list:
- description: The capability for which you are creating the business line. For example, **receivePayments**.
  name: capability
  type: string
- description: A code that represents the industry of your legal entity. For example, **4431A** for computer software stores.
  name: industryCode
  type: string
- description: Unique identifier of the [legal entity](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities__resParam_id) that owns the business line.
  name: legalEntityId
  type: string
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
schema_file: json-schema/legal-entity-business-line-info-update-schema.json
slug: legal-entity-business-line-info-update
tags:
- Payments
- Financial Services
- Fintech
title: BusinessLineInfoUpdate
---
