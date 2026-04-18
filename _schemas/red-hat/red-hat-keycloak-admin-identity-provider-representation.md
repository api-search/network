---
description: An external identity provider configured for federated authentication.
layout: schema
name: IdentityProviderRepresentation
properties_list:
- description: The unique alias for the identity provider.
  name: alias
  type: string
- description: The display name of the identity provider.
  name: displayName
  type: string
- description: The provider type identifier.
  name: providerId
  type: string
- description: Whether the identity provider is enabled.
  name: enabled
  type: boolean
- description: Provider-specific configuration.
  name: config
  type: object
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-keycloak-admin-identity-provider-representation-schema.json
slug: red-hat-keycloak-admin-identity-provider-representation
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: IdentityProviderRepresentation
---
