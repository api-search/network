---
description: 'An error object is associated with individual DPA failures in a given batch (assuming a COMPLETED_WITH_ERRORS response). Please note: In the event of a SUCCESSFUL response, this error object may be sent as NULL.'
layout: schema
name: Error
properties_list:
- description: HTTP status code associated with the Digital Payment Application (DPA) item error.
  name: status
  type: integer
- description: Reason for receiving an error for the Digital Payment Application (DPA) item.
  name: reason
  type: string
- description: Additional details on the Digital Payment Application (DPA) item error.
  name: message
  type: string
- description: List of errors associated with a failed Digital Payment Application (DPA) item action.
  name: errordetail
  type: array
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-checkout-solutions-error-schema.json
slug: mastercard-checkout-solutions-error
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Error
---
