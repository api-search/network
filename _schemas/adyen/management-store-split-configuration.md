---
description: StoreSplitConfiguration schema from Adyen API
layout: schema
name: StoreSplitConfiguration
properties_list:
- description: The [unique identifier of the balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__queryParam_id) to which the split amount must be booked, depending
  name: balanceAccountId
  type: string
- description: The unique identifier of the [split configuration profile](https://docs.adyen.com/marketplaces-and-platforms/automatic-split-configuration/create-split-configuration/).
  name: splitConfigurationId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-store-split-configuration-schema.json
slug: management-store-split-configuration
tags:
- Payments
- Financial Services
- Fintech
title: StoreSplitConfiguration
---
