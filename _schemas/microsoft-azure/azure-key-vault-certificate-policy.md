---
description: Management policy for a certificate.
layout: schema
name: CertificatePolicy
properties_list:
- description: ''
  name: id
  type: string
- description: Properties of the key pair.
  name: key_props
  type: object
- description: Properties of the secret backing a certificate.
  name: secret_props
  type: object
- description: Properties of the X509 component.
  name: x509_props
  type: object
- description: Parameters for the issuer of the X509 component.
  name: issuer
  type: object
- description: ''
  name: lifetime_actions
  type: array
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-key-vault-certificate-policy-schema.json
slug: azure-key-vault-certificate-policy
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: CertificatePolicy
---
