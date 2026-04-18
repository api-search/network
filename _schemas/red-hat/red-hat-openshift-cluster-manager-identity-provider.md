---
description: Represents an identity provider configured for cluster authentication.
layout: schema
name: IdentityProvider
properties_list:
- description: The unique identifier of the identity provider.
  name: id
  type: string
- description: The display name of the identity provider.
  name: name
  type: string
- description: The type of identity provider.
  name: type
  type: string
- description: The method used to map identities to users.
  name: mapping_method
  type: string
- description: GitHub-specific identity provider configuration.
  name: github
  type: object
- description: LDAP-specific identity provider configuration.
  name: ldap
  type: object
- description: OpenID Connect identity provider configuration.
  name: openid
  type: object
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-openshift-cluster-manager-identity-provider-schema.json
slug: red-hat-openshift-cluster-manager-identity-provider
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: IdentityProvider
---
