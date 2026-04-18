---
description: A cookie persistence profile that maintains session persistence by inserting or reading HTTP cookies.
layout: schema
name: CookiePersistenceProfile
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
- description: Whether to always send the cookie.
  name: alwaysSend
  type: string
- description: Cookie encryption method.
  name: cookieEncryption
  type: string
- description: Name of the persistence cookie.
  name: cookieName
  type: string
- description: Parent profile.
  name: defaultsFrom
  type: string
- description: ''
  name: description
  type: string
- description: Cookie expiration time.
  name: expiration
  type: string
- description: Length of the cookie hash.
  name: hashLength
  type: integer
- description: Offset for the cookie hash.
  name: hashOffset
  type: integer
- description: Whether the cookie has the HttpOnly flag.
  name: httponly
  type: string
- description: Whether to match persistence across pools.
  name: matchAcrossPools
  type: string
- description: Whether to match persistence across virtual servers.
  name: matchAcrossServices
  type: string
- description: Whether to match persistence across all virtuals.
  name: matchAcrossVirtuals
  type: string
- description: Cookie persistence method.
  name: method
  type: string
- description: Whether to mirror persistence records.
  name: mirror
  type: string
- description: Whether to override connection limits for persisted sessions.
  name: overrideConnectionLimit
  type: string
- description: Whether the cookie has the Secure flag.
  name: secure
  type: string
- description: Persistence timeout in seconds.
  name: timeout
  type: string
provider_name: F5 Networks
provider_slug: f5-networks
schema_file: json-schema/bigip-icontrol-rest-cookie-persistence-profile-schema.json
slug: bigip-icontrol-rest-cookie-persistence-profile
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
title: CookiePersistenceProfile
---
