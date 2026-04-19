---
description: Company schema from Adyen API
layout: schema
name: Company
properties_list:
- description: References to resources connected with this company.
  name: _links
  type: object
- description: List of available data centers. Adyen has several data centers around the world.In the URL that you use for making API requests, we recommend you use the live URL prefix from the data center closest t
  name: dataCenters
  type: array
- description: Your description for the company account, maximum 300 characters
  name: description
  type: string
- description: The unique identifier of the company account.
  name: id
  type: string
- description: The legal or trading name of the company.
  name: name
  type: string
- description: Your reference to the account
  name: reference
  type: string
- description: 'The status of the company account. Possible values: * **Active**: Users can log in. Processing and payout capabilities depend on the status of the merchant account. * **Inactive**: Users can log in. P'
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-company-schema.json
slug: management-company
tags:
- Payments
- Financial Services
- Fintech
title: Company
---
