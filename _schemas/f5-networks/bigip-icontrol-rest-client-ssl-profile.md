---
description: A Client SSL profile for managing SSL/TLS connections between clients and the BIG-IP system.
layout: schema
name: ClientSslProfile
properties_list:
- description: ''
  name: kind
  type: string
- description: ''
  name: name
  type: string
- description: ''
  name: fullPath
  type: string
- description: ''
  name: generation
  type: integer
- description: ''
  name: selfLink
  type: string
- description: Alert timeout for SSL handshake.
  name: alertTimeout
  type: string
- description: Whether to allow non-SSL connections.
  name: allowNonSsl
  type: string
- description: Path to the SSL certificate file.
  name: cert
  type: string
- description: Certificate and key chain pairs.
  name: certKeyChain
  type: array
- description: Cipher suite string.
  name: ciphers
  type: string
- description: Parent profile.
  name: defaultsFrom
  type: string
- description: ''
  name: description
  type: string
- description: Path to the SSL private key file.
  name: key
  type: string
- description: SSL options.
  name: options
  type: array
- description: Client certificate verification mode.
  name: peerCertMode
  type: string
- description: Whether SSL renegotiation is allowed.
  name: renegotiation
  type: string
- description: Secure renegotiation mode.
  name: secureRenegotiation
  type: string
- description: Whether this is the default SNI profile.
  name: sniDefault
  type: string
- description: Whether SNI is required.
  name: sniRequire
  type: string
- description: Whether SSL forward proxy is enabled.
  name: sslForwardProxy
  type: string
- description: How to handle unclean SSL shutdowns.
  name: uncleanShutdown
  type: string
provider_name: F5 Networks
provider_slug: f5-networks
schema_file: json-schema/bigip-icontrol-rest-client-ssl-profile-schema.json
slug: bigip-icontrol-rest-client-ssl-profile
tags:
- API Gateway
- Application Delivery
- Automation
- Edge Computing
- Kubernetes
- Load Balancing
- Multi-Cloud
- NGINX
- Security
- WAF
title: ClientSslProfile
---
