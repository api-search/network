---
description: AndroidCertificate schema from Adyen API
layout: schema
name: AndroidCertificate
properties_list:
- description: The description that was provided when uploading the certificate.
  name: description
  type: string
- description: The file format of the certificate, as indicated by the file extension. For example, **.cert** or **.pem**.
  name: extension
  type: string
- description: The unique identifier of the certificate.
  name: id
  type: string
- description: The file name of the certificate. For example, **mycert**.
  name: name
  type: string
- description: The date when the certificate stops to be valid.
  name: notAfter
  type: string
- description: The date when the certificate starts to be valid.
  name: notBefore
  type: string
- description: The status of the certificate.
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-android-certificate-schema.json
slug: management-android-certificate
tags:
- Payments
- Financial Services
- Fintech
title: AndroidCertificate
---
