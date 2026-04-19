---
description: DisablePermitRequest schema from Adyen API
layout: schema
name: DisablePermitRequest
properties_list:
- description: The merchant account identifier, with which you want to process the transaction.
  name: merchantAccount
  type: string
- description: The permit token to disable.
  name: token
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/recurring-disable-permit-request-schema.json
slug: recurring-disable-permit-request
tags:
- Payments
- Financial Services
- Fintech
title: DisablePermitRequest
---
