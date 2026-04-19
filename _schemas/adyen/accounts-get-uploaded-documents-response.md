---
description: GetUploadedDocumentsResponse schema from Adyen API
layout: schema
name: GetUploadedDocumentsResponse
properties_list:
- description: A list of the documents and their details.
  name: documentDetails
  type: array
- description: Contains field validation errors that would prevent requests from being processed.
  name: invalidFields
  type: array
- description: The reference of a request. Can be used to uniquely identify the request.
  name: pspReference
  type: string
- description: The result code.
  name: resultCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-get-uploaded-documents-response-schema.json
slug: accounts-get-uploaded-documents-response
tags:
- Payments
- Financial Services
- Fintech
title: GetUploadedDocumentsResponse
---
