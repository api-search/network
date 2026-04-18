---
class_count: 18
classes:
- Adobe CEP Extension Manifest
- Element
- ElementCreation
- ErrorResponse
- ExpandImageRequest
- FillImageRequest
- GenerateImagesRequest
- GenerateImagesResponse
- GenerateSimilarRequest
- ImageReference
- Library
- LicenseHistoryResponse
- LicenseInfoResponse
- LicenseResponse
- MemberProfile
- ObjectCompositeRequest
- SearchResponse
- StockAsset
context_file: json-ld/adobe-creative-cloud-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adobe-creative-cloud/refs/heads/main/json-ld/adobe-creative-cloud-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adobe Creative Cloud from Adobe Creative Cloud.
layout: jsonld
name: Adobe Creative Cloud Context
namespaces:
- prefix: adobe
  uri: https://developer.adobe.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: ExtensionManifest
  type: reference
- container: ''
  name: available_entitlement
  type: reference
- container: ''
  name: category
  type: reference
- container: ''
  name: client_data
  type: reference
- container: ''
  name: comp_url
  type: reference
- container: ''
  name: contentClass
  type: string
- container: ''
  name: content_type
  type: string
- container: ''
  name: contents
  type: reference
- container: ''
  name: created_date
  type: dateTime
- container: ''
  name: creator_id
  type: integer
- container: ''
  name: creator_name
  type: string
- container: ''
  name: element_count
  type: integer
- container: ''
  name: error_code
  type: string
- container: set
  name: files
  type: string
- container: ''
  name: height
  type: integer
- container: ''
  name: id
  type: string
- container: ''
  name: image
  type: string
- container: ''
  name: is_licensed
  type: string
- container: set
  name: keywords
  type: string
- container: ''
  name: mask
  type: string
- container: ''
  name: message
  type: string
- container: ''
  name: modified_date
  type: dateTime
- container: ''
  name: name
  type: string
- container: ''
  name: nb_results
  type: integer
- container: ''
  name: negativePrompt
  type: string
- container: ''
  name: numVariations
  type: integer
- container: set
  name: outputs
  type: string
- container: ''
  name: owner
  type: reference
- container: ''
  name: placement
  type: reference
- container: ''
  name: premium_level_id
  type: integer
- container: ''
  name: prompt
  type: string
- container: set
  name: representations
  type: string
- container: set
  name: seeds
  type: string
- container: ''
  name: size
  type: reference
- container: ''
  name: source
  type: reference
- container: ''
  name: style
  type: reference
- container: ''
  name: thumbnail
  type: reference
- container: ''
  name: thumbnail_height
  type: integer
- container: ''
  name: thumbnail_url
  type: reference
- container: ''
  name: thumbnail_width
  type: integer
- container: ''
  name: title
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: width
  type: integer
property_count: 43
provider_name: Adobe Creative Cloud
provider_slug: adobe-creative-cloud
slug: adobe-creative-cloud-context
tags:
- AI/ML
- Cloud
- Creative
- Design
- Documents
- Photography
- SaaS
- Video
- JSON-LD
- Linked Data
- Semantic Web
---
