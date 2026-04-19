---
description: RequestCertificateRequest schema from Amazon Certificate Manager API
layout: schema
name: RequestCertificateRequest
properties_list:
- description: The fully qualified domain name for the certificate.
  name: DomainName
  type: string
- description: Additional FQDNs to be included in the certificate.
  name: SubjectAlternativeNames
  type: array
- description: The method to use for validation.
  name: ValidationMethod
  type: string
- description: Token to prevent duplicate requests.
  name: IdempotencyToken
  type: string
provider_name: Amazon Certificate Manager
provider_slug: amazon-certificate-manager
schema_file: json-schema/certificate-manager-request-certificate-request-schema.json
slug: certificate-manager-request-certificate-request
tags:
- AWS
- Certificates
- Encryption
- Security
- SSL
- TLS
title: RequestCertificateRequest
---
