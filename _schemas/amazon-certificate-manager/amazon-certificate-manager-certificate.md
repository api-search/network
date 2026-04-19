---
description: Represents an ACM SSL/TLS certificate with its associated metadata, domain validation, and lifecycle information.
layout: schema
name: Amazon Certificate Manager Certificate
properties_list:
- description: The Amazon Resource Name (ARN) of the certificate.
  name: certificateArn
  type: string
- description: The fully qualified domain name for the certificate.
  name: domainName
  type: string
- description: One or more domain names (subject alternative names) included in the certificate.
  name: subjectAlternativeNames
  type: array
- description: The status of the certificate.
  name: status
  type: string
- description: The source of the certificate.
  name: type
  type: string
- description: The name of the certificate authority that issued the certificate.
  name: issuer
  type: string
- description: The serial number of the certificate.
  name: serial
  type: string
- description: The algorithm used to generate the key pair.
  name: keyAlgorithm
  type: string
- description: The time at which the certificate was requested.
  name: createdAt
  type: string
- description: The time at which the certificate was issued.
  name: issuedAt
  type: string
- description: The time before which the certificate is not valid.
  name: notBefore
  type: string
- description: The time after which the certificate is not valid.
  name: notAfter
  type: string
- description: Whether the certificate is eligible for renewal.
  name: renewalEligibility
  type: string
provider_name: Amazon Certificate Manager
provider_slug: amazon-certificate-manager
schema_file: json-schema/amazon-certificate-manager-certificate-schema.json
slug: amazon-certificate-manager-certificate
tags:
- AWS
- Certificates
- Encryption
- Security
- SSL
- TLS
title: Amazon Certificate Manager Certificate
---
