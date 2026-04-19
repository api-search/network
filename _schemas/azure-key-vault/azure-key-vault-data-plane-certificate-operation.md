---
description: A certificate operation is returned in case of asynchronous requests.
layout: schema
name: CertificateOperation
properties_list:
- description: The certificate id.
  name: id
  type: string
- description: The certificate signing request (CSR) that is being used in the certificate operation.
  name: csr
  type: string
- description: Indicates if cancellation was requested on the certificate operation.
  name: cancellation_requested
  type: boolean
- description: Status of the certificate operation.
  name: status
  type: string
- description: The status details of the certificate operation.
  name: status_details
  type: string
- description: Location which contains the result of the certificate operation.
  name: target
  type: string
- description: Identifier for the certificate operation.
  name: request_id
  type: string
provider_name: Azure Key Vault
provider_slug: azure-key-vault
schema_file: json-schema/azure-key-vault-data-plane-certificate-operation-schema.json
slug: azure-key-vault-data-plane-certificate-operation
tags:
- Certificates
- Cloud Security
- Cryptography
- Key Management
- Secrets Management
- Security
title: CertificateOperation
---
