---
description: 'A limited number of DPA fields can be changed using the __UPDATE__ action. These are `supportedCardBrands`, `supportedCheckoutTypes`, `dpaPresentationName`, `originDomains`, `debitTokenRequested`, `merchantCategoryCodes`, `defaultAcquirerBin`, `defaultAcquirerMerchantId`, `defaultMerchantCategoryCode`, `acquirerIca`, `acquirerBin` and `acquirerMerchantId`. __Note__: All DPA data from the original request (including non-updatable fields, such as `dpaUri` and `dpaAddress` if previously passed) will also need to be provided unchanged in the __PUT__ request for the update operation to process successfully. Any alterations contained in the request made outside of these updatable fields will cause the request to fail.'
layout: schema
name: UpdateDpaRequest
properties_list: []
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-unified-checkout-solutions-update-dpa-request-schema.json
slug: mastercard-unified-checkout-solutions-update-dpa-request
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: UpdateDpaRequest
---
