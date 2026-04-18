---
description: A client application registered in a Keycloak realm for authentication.
layout: schema
name: Client
properties_list:
- description: The unique identifier of the client.
  name: id
  type: string
- description: The client identifier used in authentication flows.
  name: clientId
  type: string
- description: The display name of the client.
  name: name
  type: string
- description: A description of the client.
  name: description
  type: string
- description: Whether the client is enabled.
  name: enabled
  type: boolean
- description: The authentication protocol.
  name: protocol
  type: string
- description: Whether the client is public (no client secret).
  name: publicClient
  type: boolean
- description: The root URL of the client application.
  name: rootUrl
  type: string
- description: Allowed redirect URIs after authentication.
  name: redirectUris
  type: array
- description: Allowed web origins for CORS.
  name: webOrigins
  type: array
- description: Whether service accounts are enabled.
  name: serviceAccountsEnabled
  type: boolean
- description: Whether authorization services are enabled.
  name: authorizationServicesEnabled
  type: boolean
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-keycloak-admin-client-schema.json
slug: red-hat-keycloak-admin-client
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: Client
---
