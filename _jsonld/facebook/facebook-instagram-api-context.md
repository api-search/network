---
class_count: 3
classes:
- InstagramUser
- InstagramMedia
- InstagramComment
context_file: json-ld/facebook-instagram-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/facebook/refs/heads/main/json-ld/facebook-instagram-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Facebook Instagram Api from Facebook.
layout: jsonld
name: Facebook Instagram Api Context
namespaces:
- prefix: fb
  uri: https://developers.facebook.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: username
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: biography
  type: string
- container: ''
  name: followersCount
  type: integer
- container: ''
  name: mediaCount
  type: integer
- container: ''
  name: caption
  type: string
- container: ''
  name: mediaType
  type: string
- container: ''
  name: mediaUrl
  type: reference
- container: ''
  name: permalink
  type: reference
- container: ''
  name: likeCount
  type: integer
- container: ''
  name: commentsCount
  type: integer
property_count: 11
provider_name: Facebook
provider_slug: facebook
slug: facebook-instagram-api-context
tags:
- Advertising
- Content Publishing
- Messaging
- Social Media
- Social Networking
- JSON-LD
- Linked Data
- Semantic Web
---
