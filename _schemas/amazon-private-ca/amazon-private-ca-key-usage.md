---
description: Defines one or more purposes for which the key contained in the certificate can be used. Default value for each option is false.
layout: schema
name: KeyUsage
properties_list:
- description: ''
  name: DigitalSignature
  type: object
- description: ''
  name: NonRepudiation
  type: object
- description: ''
  name: KeyEncipherment
  type: object
- description: ''
  name: DataEncipherment
  type: object
- description: ''
  name: KeyAgreement
  type: object
- description: ''
  name: KeyCertSign
  type: object
- description: ''
  name: CRLSign
  type: object
- description: ''
  name: EncipherOnly
  type: object
- description: ''
  name: DecipherOnly
  type: object
provider_name: Amazon Private CA
provider_slug: amazon-private-ca
schema_file: json-schema/amazon-private-ca-key-usage-schema.json
slug: amazon-private-ca-key-usage
tags:
- AWS
- Certificate Authority
- Certificates
- PKI
- Security
- X.509
- TLS
- IoT
title: KeyUsage
---
