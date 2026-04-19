---
description: SessionResultResponse schema from Adyen API
layout: schema
name: SessionResultResponse
properties_list:
- description: A unique identifier of the session.
  name: id
  type: string
- description: 'The status of the session. The status included in the response doesn''t get updated. Don''t make the request again to check for payment status updates. Possible values: * **completed** – The shopper com'
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-session-result-response-schema.json
slug: checkout-session-result-response
tags:
- Payments
- Financial Services
- Fintech
title: SessionResultResponse
---
