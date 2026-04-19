---
description: ModifyRequest schema from Adyen API
layout: schema
name: ModifyRequest
properties_list:
- description: This field contains additional data, which may be required for a particular payout request.
  name: additionalData
  type: object
- description: The merchant account identifier, with which you want to process the transaction.
  name: merchantAccount
  type: string
- description: The PSP reference received in the `/submitThirdParty` response.
  name: originalReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/payouts-modify-request-schema.json
slug: payouts-modify-request
tags:
- Payments
- Financial Services
- Fintech
title: ModifyRequest
---
