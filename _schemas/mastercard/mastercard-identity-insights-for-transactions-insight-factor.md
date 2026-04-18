---
description: The insight factor is represented numerically using a range from 0 (no risk data) to 5 (high risk). Each numerical value and its associated risk representation is shown below. * `0` - Represents an unknown risk because no data on this device is available. * `1` - Represents a no or low risk request. * `2` - Represents a low risk request. * `3` - Represents a medium risk request. * `4` - Represents a high risk request. * `5` - Represents a very high risk request. The insight factor is typically used to identify scenarios where a service provider may want to introduce consumer friction on the authorization process to validate the identity of the consumer. Example usage by a service provider may be to implement controls such as multifactor authentication for calculated risk factors of `3` or `4` and request blocking for risk factors of `5`.
layout: schema
name: InsightFactor
properties_list: []
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-identity-insights-for-transactions-insight-factor-schema.json
slug: mastercard-identity-insights-for-transactions-insight-factor
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: InsightFactor
---
