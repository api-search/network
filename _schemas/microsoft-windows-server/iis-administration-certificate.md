---
description: An SSL/TLS certificate associated with an HTTPS binding.
layout: schema
name: Certificate
properties_list:
- description: The friendly name of the certificate.
  name: name
  type: string
- description: The unique identifier of the certificate resource.
  name: id
  type: string
- description: The certificate issuer distinguished name.
  name: issued_by
  type: string
- description: The certificate subject distinguished name.
  name: subject
  type: string
- description: The SHA-1 thumbprint of the certificate.
  name: thumbprint
  type: string
- description: The expiration date of the certificate.
  name: valid_to
  type: string
provider_name: Microsoft Windows Server
provider_slug: microsoft-windows-server
schema_file: json-schema/iis-administration-certificate-schema.json
slug: iis-administration-certificate
tags:
- Datacenter
- Enterprise
- Infrastructure
- Microsoft
- Operating System
- Server Management
- Windows Server
- Windows Server 2025
title: Certificate
---
