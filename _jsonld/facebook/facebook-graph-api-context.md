---
class_count: 5
classes:
- User
- Post
- Page
- Photo
- Comment
context_file: json-ld/facebook-graph-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/facebook/refs/heads/main/json-ld/facebook-graph-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Facebook Graph Api from Facebook.
layout: jsonld
name: Facebook Graph Api Context
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
  name: name
  type: string
- container: ''
  name: email
  type: string
- container: ''
  name: description
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: createdTime
  type: dateTime
- container: ''
  name: updatedTime
  type: dateTime
- container: ''
  name: link
  type: reference
- container: ''
  name: permalinkUrl
  type: reference
- container: ''
  name: category
  type: string
- container: ''
  name: fanCount
  type: integer
- container: ''
  name: website
  type: reference
- container: ''
  name: likeCount
  type: integer
- container: ''
  name: width
  type: integer
- container: ''
  name: height
  type: integer
property_count: 14
provider_name: Facebook
provider_slug: facebook
slug: facebook-graph-api-context
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
