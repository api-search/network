---
description: <p/> <p>Specifies the X.509 extension information for a certificate.</p> <p>Extensions present in <code>CustomExtensions</code> follow the <code>ApiPassthrough</code> <a href="https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html#template-order-of-operations">template rules</a>. </p>
layout: schema
name: CustomExtension
properties_list:
- description: ''
  name: ObjectIdentifier
  type: object
- description: ''
  name: Value
  type: object
- description: ''
  name: Critical
  type: object
provider_name: Amazon Private CA
provider_slug: amazon-private-ca
schema_file: json-schema/amazon-private-ca-custom-extension-schema.json
slug: amazon-private-ca-custom-extension
tags:
- AWS
- Certificate Authority
- Certificates
- PKI
- Security
- X.509
- TLS
- IoT
title: CustomExtension
---
