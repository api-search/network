---
description: DisablePermitResult schema from Adyen API
layout: schema
name: DisablePermitResult
properties_list:
- description: A unique reference associated with the request. This value is globally unique; quote it when communicating with us about this request.
  name: pspReference
  type: string
- description: Status of the disable request.
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/recurring-disable-permit-result-schema.json
slug: recurring-disable-permit-result
tags:
- Payments
- Financial Services
- Fintech
title: DisablePermitResult
---
