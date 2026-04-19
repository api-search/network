---
description: Permissions designate which private CA actions can be performed by an Amazon Web Services service or entity. In order for ACM to automatically renew private certificates, you must give the ACM service principal all available permissions (<code>IssueCertificate</code>, <code>GetCertificate</code>, and <code>ListPermissions</code>). Permissions can be assigned with the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreatePermission.html">CreatePermission</a> action, removed with the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePermission.html">DeletePermission</a> action, and listed with the <a href="https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListPermissions.html">ListPermissions</a> action.
layout: schema
name: Permission
properties_list:
- description: ''
  name: CertificateAuthorityArn
  type: object
- description: ''
  name: CreatedAt
  type: object
- description: ''
  name: Principal
  type: object
- description: ''
  name: SourceAccount
  type: object
- description: ''
  name: Actions
  type: object
- description: ''
  name: Policy
  type: object
provider_name: Amazon Private CA
provider_slug: amazon-private-ca
schema_file: json-schema/amazon-private-ca-permission-schema.json
slug: amazon-private-ca-permission
tags:
- AWS
- Certificate Authority
- Certificates
- PKI
- Security
- X.509
- TLS
- IoT
title: Permission
---
