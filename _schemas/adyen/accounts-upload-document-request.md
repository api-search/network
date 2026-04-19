---
description: UploadDocumentRequest schema from Adyen API
layout: schema
name: UploadDocumentRequest
properties_list:
- description: The content of the document, in Base64-encoded string format. To learn about document requirements, refer to [Verification checks](https://docs.adyen.com/marketplaces-and-platforms/classic/verificatio
  name: documentContent
  type: string
- description: Details of the document being submitted.
  name: documentDetail
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounts-upload-document-request-schema.json
slug: accounts-upload-document-request
tags:
- Payments
- Financial Services
- Fintech
title: UploadDocumentRequest
---
