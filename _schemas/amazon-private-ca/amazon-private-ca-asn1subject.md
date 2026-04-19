---
description: Contains information about the certificate subject. The <code>Subject</code> field in the certificate identifies the entity that owns or controls the public key in the certificate. The entity can be a user, computer, device, or service. The <code>Subject </code>must contain an X.500 distinguished name (DN). A DN is a sequence of relative distinguished names (RDNs). The RDNs are separated by commas in the certificate.
layout: schema
name: ASN1Subject
properties_list:
- description: ''
  name: Country
  type: object
- description: ''
  name: Organization
  type: object
- description: ''
  name: OrganizationalUnit
  type: object
- description: ''
  name: DistinguishedNameQualifier
  type: object
- description: ''
  name: State
  type: object
- description: ''
  name: CommonName
  type: object
- description: ''
  name: SerialNumber
  type: object
- description: ''
  name: Locality
  type: object
- description: ''
  name: Title
  type: object
- description: ''
  name: Surname
  type: object
- description: ''
  name: GivenName
  type: object
- description: ''
  name: Initials
  type: object
- description: ''
  name: Pseudonym
  type: object
- description: ''
  name: GenerationQualifier
  type: object
- description: ''
  name: CustomAttributes
  type: object
provider_name: Amazon Private CA
provider_slug: amazon-private-ca
schema_file: json-schema/amazon-private-ca-asn1subject-schema.json
slug: amazon-private-ca-asn1subject
tags:
- AWS
- Certificate Authority
- Certificates
- PKI
- Security
- X.509
- TLS
- IoT
title: ASN1Subject
---
