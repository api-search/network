---
class_count: 11
classes:
- Comment
- CommentList
- ContainerResponse
- CreateContainerRequest
- ErrorResponse
- InsightsResponse
- Media
- MediaList
- Paging
- SuccessResponse
- User
context_file: json-ld/instagram-graph-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/instagram/refs/heads/main/json-ld/instagram-graph-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Instagram Graph Api from Instagram.
layout: jsonld
name: Instagram Graph Api Context
namespaces:
- prefix: ig
  uri: https://developers.facebook.com/docs/instagram-api/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: access_token
  type: string
- container: ''
  name: alt_text
  type: string
- container: ''
  name: biography
  type: string
- container: ''
  name: caption
  type: string
- container: ''
  name: comments_count
  type: integer
- container: ''
  name: cursors
  type: reference
- container: set
  name: data
  type: string
- container: ''
  name: error
  type: reference
- container: ''
  name: followers_count
  type: integer
- container: ''
  name: follows_count
  type: integer
- container: ''
  name: hidden
  type: boolean
- container: ''
  name: id
  type: string
- container: ''
  name: image_url
  type: string
- container: ''
  name: is_carousel_item
  type: boolean
- container: ''
  name: is_comment_enabled
  type: boolean
- container: ''
  name: is_shared_to_feed
  type: boolean
- container: ''
  name: like_count
  type: integer
- container: ''
  name: location_id
  type: string
- container: ''
  name: media_count
  type: integer
- container: ''
  name: media_type
  type: string
- container: ''
  name: media_url
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: next
  type: string
- container: ''
  name: paging
  type: string
- container: ''
  name: parent_id
  type: string
- container: ''
  name: permalink
  type: string
- container: ''
  name: previous
  type: string
- container: ''
  name: profile_picture_url
  type: string
- container: ''
  name: shortcode
  type: string
- container: ''
  name: success
  type: boolean
- container: ''
  name: text
  type: string
- container: ''
  name: thumbnail_url
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: set
  name: user_tags
  type: string
- container: ''
  name: username
  type: string
- container: ''
  name: video_url
  type: string
- container: ''
  name: website
  type: string
property_count: 37
provider_name: Instagram
provider_slug: instagram
slug: instagram-graph-api-context
tags:
- Instagram
- Meta
- Photos
- Social Media
- Videos
- Content Publishing
- JSON-LD
- Linked Data
- Semantic Web
---
