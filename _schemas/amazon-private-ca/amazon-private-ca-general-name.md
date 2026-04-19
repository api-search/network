---
description: Describes an ASN.1 X.400 <code>GeneralName</code> as defined in <a href="https://datatracker.ietf.org/doc/html/rfc5280">RFC 5280</a>. Only one of the following naming options should be provided. Providing more than one option results in an <code>InvalidArgsException</code> error.
layout: schema
name: GeneralName
properties_list:
- description: ''
  name: OtherName
  type: object
- description: ''
  name: Rfc822Name
  type: object
- description: ''
  name: DnsName
  type: object
- description: ''
  name: DirectoryName
  type: object
- description: ''
  name: EdiPartyName
  type: object
- description: ''
  name: UniformResourceIdentifier
  type: object
- description: ''
  name: IpAddress
  type: object
- description: ''
  name: RegisteredId
  type: object
provider_name: Amazon Private CA
provider_slug: amazon-private-ca
schema_file: json-schema/amazon-private-ca-general-name-schema.json
slug: amazon-private-ca-general-name
tags:
- AWS
- Certificate Authority
- Certificates
- PKI
- Security
- X.509
- TLS
- IoT
title: GeneralName
---
