---
description: Validity of the API request. It protects the API from unauthorized request or man-in-the-middle (MITM) attacks <br/>For example, if the validity of the API request is set for a maximum of 5 minutes (including retry attempts), and someone tries to post the same request after 5 minutes, then the system rejects the API request without processing.
layout: schema
name: RequestValidityTime
properties_list:
- description: The date and time after which the request is considered as invalid. If the timestamp of the institution is greater than this timestamp, the API request is considered as expired and is returned.<br/>Th
  name: dataValidUntilTimestamp
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-card-issuance-request-validity-time-schema.json
slug: mastercard-card-issuance-request-validity-time
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: RequestValidityTime
---
