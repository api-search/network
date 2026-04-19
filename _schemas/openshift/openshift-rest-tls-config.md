---
description: TLS configuration for the route. Determines how TLS connections are handled at the router.
layout: schema
name: TLSConfig
properties_list:
- description: Indicates termination type. Edge terminates TLS at the router, passthrough forwards encrypted traffic to the backend, and re-encrypt terminates at the router and re-encrypts to the backend.
  name: termination
  type: string
- description: PEM-encoded certificate for the route. Required for edge and re-encrypt termination if not using a default certificate.
  name: certificate
  type: string
- description: PEM-encoded private key for the route certificate.
  name: key
  type: string
- description: PEM-encoded CA certificate chain used to verify client certificates.
  name: caCertificate
  type: string
- description: PEM-encoded CA certificate used to verify the backend server certificate. Only applicable for re-encrypt termination.
  name: destinationCACertificate
  type: string
- description: Policy for handling insecure (HTTP) traffic when TLS is configured. None disables insecure traffic, Allow permits it, Redirect sends a 301 redirect to the HTTPS URL.
  name: insecureEdgeTerminationPolicy
  type: string
provider_name: OpenShift
provider_slug: openshift
schema_file: json-schema/openshift-rest-tls-config-schema.json
slug: openshift-rest-tls-config
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
title: TLSConfig
---
