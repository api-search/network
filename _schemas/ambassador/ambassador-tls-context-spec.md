---
description: Specification for a TLSContext resource
layout: schema
name: TLSContextSpec
properties_list:
- description: Hostnames this TLSContext applies to
  name: hosts
  type: array
- description: Name of the Kubernetes Secret containing TLS certificates
  name: secret
  type: string
- description: Path to the certificate chain PEM file (alternative to secret)
  name: cert_chain_file
  type: string
- description: Path to the private key PEM file (alternative to secret)
  name: private_key_file
  type: string
- description: Name of the Kubernetes Secret containing CA certificates for client verification
  name: ca_secret
  type: string
- description: Whether client TLS certificates are required (mTLS)
  name: cert_required
  type: boolean
- description: Minimum TLS version to accept
  name: min_tls_version
  type: string
- description: Maximum TLS version to accept
  name: max_tls_version
  type: string
- description: Allowed TLS cipher suites
  name: cipher_suites
  type: array
- description: Allowed ECDH curves
  name: ecdh_curves
  type: array
- description: ALPN protocols to advertise
  name: alpn_protocols
  type: string
- description: Port number from which to redirect cleartext traffic to TLS
  name: redirect_cleartext_from
  type: integer
- description: SNI hostname to present for outbound TLS connections
  name: sni
  type: string
- description: Ambassador IDs that should use this TLSContext
  name: ambassador_id
  type: array
provider_name: Ambassador
provider_slug: ambassador
schema_file: json-schema/ambassador-tls-context-spec-schema.json
slug: ambassador-tls-context-spec
tags:
- API Development
- Gateways
- Ingress
- Kubernetes
- Mock Servers
- Mocks
- Platform
- Testing
title: TLSContextSpec
---
