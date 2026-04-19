---
class_count: 4
classes:
- RequestCertificateRequest
- RequestCertificateResponse
- ListCertificatesResponse
- DescribeCertificateResponse
context_file: json-ld/amazon-certificate-manager-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amazon-certificate-manager/refs/heads/main/json-ld/amazon-certificate-manager-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amazon Certificate Manager from Amazon Certificate Manager.
layout: jsonld
name: Amazon Certificate Manager Context
namespaces:
- prefix: acm
  uri: https://aws.amazon.com/certificate-manager/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: domainName
  type: string
- container: set
  name: subjectAlternativeNames
  type: string
- container: ''
  name: validationMethod
  type: string
- container: ''
  name: idempotencyToken
  type: string
- container: ''
  name: certificateArn
  type: string
- container: set
  name: certificateSummaryList
  type: string
- container: ''
  name: nextToken
  type: string
- container: ''
  name: certificate
  type: string
property_count: 8
provider_name: Amazon Certificate Manager
provider_slug: amazon-certificate-manager
slug: amazon-certificate-manager-context
tags:
- AWS
- Certificates
- Encryption
- Security
- SSL
- TLS
- JSON-LD
- Linked Data
- Semantic Web
---
