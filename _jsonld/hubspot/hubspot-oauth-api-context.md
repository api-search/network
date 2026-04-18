---
class_count: 4
classes:
- AccessTokenMetadata
- RefreshTokenMetadata
- TokenRequest
- TokenResponse
context_file: json-ld/hubspot-oauth-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-oauth-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot Oauth Api from HubSpot.
layout: jsonld
name: Hubspot Oauth Api Context
namespaces:
- prefix: hubspot
  uri: https://developers.hubspot.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: token
  type: string
- container: ''
  name: appId
  type: integer
- container: ''
  name: hubId
  type: integer
- container: ''
  name: userId
  type: integer
- container: ''
  name: user
  type: string
- container: ''
  name: hubDomain
  type: string
- container: set
  name: scopes
  type: string
- container: ''
  name: tokenType
  type: string
- container: ''
  name: expiresIn
  type: integer
- container: ''
  name: clientId
  type: string
- container: ''
  name: grantType
  type: string
- container: ''
  name: clientSecret
  type: string
- container: ''
  name: redirectUri
  type: string
- container: ''
  name: code
  type: string
- container: ''
  name: refreshToken
  type: string
- container: ''
  name: accessToken
  type: string
- container: ''
  name: idToken
  type: string
property_count: 17
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-oauth-api-context
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Operations
- Sales
- JSON-LD
- Linked Data
- Semantic Web
---
