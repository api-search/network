---
description: Contains configuration information for your private certificate authority (CA). This includes information about the class of public key algorithm and the key pair that your private CA creates when it issues a certificate. It also includes the signature algorithm that it uses when issuing certificates, and its X.500 distinguished name. You must specify this information when you call the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html">CreateCertificateAuthority</a> action.
layout: schema
name: CertificateAuthorityConfiguration
properties_list:
- description: ''
  name: KeyAlgorithm
  type: object
- description: ''
  name: SigningAlgorithm
  type: object
- description: ''
  name: Subject
  type: object
- description: ''
  name: CsrExtensions
  type: object
provider_name: Amazon Private CA
provider_slug: amazon-private-ca
schema_file: json-schema/amazon-private-ca-certificate-authority-configuration-schema.json
slug: amazon-private-ca-certificate-authority-configuration
tags:
- AWS
- Certificate Authority
- Certificates
- PKI
- Security
- X.509
- TLS
- IoT
title: CertificateAuthorityConfiguration
---
