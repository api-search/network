---
description: Contains information about your private certificate authority (CA). Your private CA can issue and revoke X.509 digital certificates. Digital certificates verify that the entity named in the certificate <b>Subject</b> field owns or controls the public key contained in the <b>Subject Public Key Info</b> field. Call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a> action to create your private CA. You must then call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCertificate.html">GetCertificateAuthorityCertificate</a> action to retrieve a private CA certificate signing request (CSR). Sign the CSR with your Amazon Web Services Private CA-hosted or on-premises root or subordinate CA certificate. Call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ImportCertificateAuthorityCertificate.html">ImportCertificateAuthorityCertificate</a>
  action to import the signed certificate into Certificate Manager (ACM).
layout: schema
name: CertificateAuthority
properties_list:
- description: ''
  name: Arn
  type: object
- description: ''
  name: OwnerAccount
  type: object
- description: ''
  name: CreatedAt
  type: object
- description: ''
  name: LastStateChangeAt
  type: object
- description: ''
  name: Type
  type: object
- description: ''
  name: Serial
  type: object
- description: ''
  name: Status
  type: object
- description: ''
  name: NotBefore
  type: object
- description: ''
  name: NotAfter
  type: object
- description: ''
  name: FailureReason
  type: object
- description: ''
  name: CertificateAuthorityConfiguration
  type: object
- description: ''
  name: RevocationConfiguration
  type: object
- description: ''
  name: RestorableUntil
  type: object
- description: ''
  name: KeyStorageSecurityStandard
  type: object
- description: ''
  name: UsageMode
  type: object
provider_name: Amazon Private CA
provider_slug: amazon-private-ca
schema_file: json-schema/amazon-private-ca-certificate-authority-schema.json
slug: amazon-private-ca-certificate-authority
tags:
- AWS
- Certificate Authority
- Certificates
- PKI
- Security
- X.509
- TLS
- IoT
title: CertificateAuthority
---
