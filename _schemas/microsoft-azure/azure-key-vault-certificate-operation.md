---
description: A certificate operation is returned in case of asynchronous requests.
layout: schema
name: CertificateOperation
properties_list:
- description: ''
  name: id
  type: string
- description: ''
  name: issuer
  type: object
- description: The certificate signing request (CSR) in base64.
  name: csr
  type: string
- description: ''
  name: cancellation_requested
  type: boolean
- description: ''
  name: status
  type: string
- description: ''
  name: status_details
  type: string
- description: ''
  name: error
  type: object
- description: ''
  name: target
  type: string
- description: ''
  name: request_id
  type: string
provider_name: Microsoft Azure
provider_slug: microsoft-azure
schema_file: json-schema/azure-key-vault-certificate-operation-schema.json
slug: azure-key-vault-certificate-operation
tags:
- API Management
- Cloud
- Cloud Computing
- Enterprise
- Infrastructure as a Service
- Platform as a Service
- T1
title: CertificateOperation
---
