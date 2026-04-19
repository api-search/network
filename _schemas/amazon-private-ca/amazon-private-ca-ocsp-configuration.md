---
description: <p>Contains information to enable and configure Online Certificate Status Protocol (OCSP) for validating certificate revocation status.</p> <p>When you revoke a certificate, OCSP responses may take up to 60 minutes to reflect the new status.</p>
layout: schema
name: OcspConfiguration
properties_list:
- description: ''
  name: Enabled
  type: object
- description: ''
  name: OcspCustomCname
  type: object
provider_name: Amazon Private CA
provider_slug: amazon-private-ca
schema_file: json-schema/amazon-private-ca-ocsp-configuration-schema.json
slug: amazon-private-ca-ocsp-configuration
tags:
- AWS
- Certificate Authority
- Certificates
- PKI
- Security
- X.509
- TLS
- IoT
title: OcspConfiguration
---
