---
description: StoredValueStatusChangeResponse schema from Adyen API
layout: schema
name: StoredValueStatusChangeResponse
properties_list:
- description: 'Authorisation code: * When the payment is authorised, this field holds the authorisation code for the payment. * When the payment is not authorised, this field is empty.'
  name: authCode
  type: string
- description: The balance currently on the payment method.
  name: currentBalance
  type: object
- description: Adyen's 16-character string reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request.
  name: pspReference
  type: string
- description: If the transaction is refused or an error occurs, this field holds Adyen's mapped reason for the refusal or a description of the error. When a transaction fails, the authorisation response includes `r
  name: refusalReason
  type: string
- description: 'The result of the payment. Possible values: * **Success** – The operation has been completed successfully. * **Refused** – The operation was refused. The reason is given in the `refusalReason` field. '
  name: resultCode
  type: string
- description: Raw refusal reason received from the third party, where available
  name: thirdPartyRefusalReason
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/stored-value-stored-value-status-change-response-schema.json
slug: stored-value-stored-value-status-change-response
tags:
- Payments
- Financial Services
- Fintech
title: StoredValueStatusChangeResponse
---
