---
description: An HTTP profile that defines how the BIG-IP processes HTTP traffic for a virtual server.
layout: schema
name: HttpProfile
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
- description: Whether to accept X-Forwarded-For headers from clients.
  name: acceptXff
  type: string
- description: ''
  name: appService
  type: string
- description: Realm for HTTP Basic authentication challenges.
  name: basicAuthRealm
  type: string
- description: Parent profile from which this profile inherits settings.
  name: defaultsFrom
  type: string
- description: ''
  name: description
  type: string
- description: List of cookie names to encrypt.
  name: encryptCookies
  type: array
- description: ''
  name: enforcement
  type: object
- description: Fallback host for HTTP redirects.
  name: fallbackHost
  type: string
- description: HTTP status codes that trigger fallback redirection.
  name: fallbackStatusCodes
  type: array
- description: Regular expression for headers to remove from responses.
  name: headerErase
  type: string
- description: Header to insert into requests.
  name: headerInsert
  type: string
- description: Whether to insert an X-Forwarded-For header.
  name: insertXforwardedFor
  type: string
- description: Whether to rewrite HTTP connections for OneConnect.
  name: oneconnectTransformations
  type: string
- description: Redirect rewrite mode.
  name: redirectRewrite
  type: string
- description: How to handle chunked requests.
  name: requestChunking
  type: string
- description: How to handle chunked responses.
  name: responseChunking
  type: string
- description: Server agent string to include in responses.
  name: serverAgentName
  type: string
- description: Hostname to use in Via headers.
  name: viaHostName
  type: string
- description: Via header handling for requests.
  name: viaRequest
  type: string
- description: Via header handling for responses.
  name: viaResponse
  type: string
- description: Alternative header names for X-Forwarded-For.
  name: xffAlternativeNames
  type: array
provider_name: F5 Networks
provider_slug: f5-networks
schema_file: json-schema/bigip-icontrol-rest-http-profile-schema.json
slug: bigip-icontrol-rest-http-profile
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
title: HttpProfile
---
