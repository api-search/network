---
description: A Keycloak realm representing an isolated tenant for identity management.
layout: schema
name: Realm
properties_list:
- description: The unique identifier of the realm.
  name: id
  type: string
- description: The name of the realm.
  name: realm
  type: string
- description: The display name of the realm.
  name: displayName
  type: string
- description: Whether the realm is enabled.
  name: enabled
  type: boolean
- description: Whether user self-registration is allowed.
  name: registrationAllowed
  type: boolean
- description: Whether users can log in with their email address.
  name: loginWithEmailAllowed
  type: boolean
- description: Whether duplicate emails are allowed.
  name: duplicateEmailsAllowed
  type: boolean
- description: Whether password reset is enabled.
  name: resetPasswordAllowed
  type: boolean
- description: The SSL requirement policy.
  name: sslRequired
  type: string
- description: The access token lifespan in seconds.
  name: accessTokenLifespan
  type: integer
- description: The SSO session idle timeout in seconds.
  name: ssoSessionIdleTimeout
  type: integer
- description: The maximum SSO session lifespan in seconds.
  name: ssoSessionMaxLifespan
  type: integer
provider_name: Red Hat
provider_slug: red-hat
schema_file: json-schema/red-hat-keycloak-admin-realm-schema.json
slug: red-hat-keycloak-admin-realm
tags:
- Cloud
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- Linux
- Open Source
title: Realm
---
