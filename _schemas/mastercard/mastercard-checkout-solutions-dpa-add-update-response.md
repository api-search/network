---
description: The DpaAddUpdateResponse contains the Batch ID for the submitted Digital Payment Application (DPA) batch. The Batch ID can be used to retrieve the status of the batch.
layout: schema
name: DpaAddUpdateResponse
properties_list:
- description: A unique identifier associated with the submitted Digital Payment Application (DPA) batch. The Batch ID can be used to retrieve the status of the batch by calling GET DPA status endpoint.
  name: batchId
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-checkout-solutions-dpa-add-update-response-schema.json
slug: mastercard-checkout-solutions-dpa-add-update-response
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: DpaAddUpdateResponse
---
