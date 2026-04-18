---
class_count: 16
classes:
- ActionJSONRequest
- Adobe Photoshop UXP Plugin Manifest
- ArtboardCreateRequest
- DepthBlurRequest
- DocumentCreateRequest
- DocumentManifestRequest
- DocumentOperationsRequest
- FillMaskedAreasRequest
- PhotoshopActionsRequest
- ProductCropRequest
- RemoveBackgroundRequest
- RenditionCreateRequest
- SmartObjectRequest
- StorageInput
- StorageOutput
- TextEditRequest
context_file: json-ld/adobe-photoshop-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adobe-photoshop/refs/heads/main/json-ld/adobe-photoshop-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adobe Photoshop from Adobe Photoshop.
layout: jsonld
name: Adobe Photoshop Context
namespaces:
- prefix: ps
  uri: https://developer.adobe.com/photoshop/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: addon
  type: reference
- container: ''
  name: author
  type: string
- container: ''
  name: backgroundColor
  type: reference
- container: ''
  name: colorDecontamination
  type: integer
- container: ''
  name: description
  type: string
- container: set
  name: entrypoints
  type: string
- container: ''
  name: host
  type: reference
- container: ''
  name: href
  type: string
- container: set
  name: icons
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: image
  type: reference
- container: set
  name: inputs
  type: string
- container: set
  name: keywords
  type: string
- container: ''
  name: main
  type: string
- container: ''
  name: manifestVersion
  type: integer
- container: set
  name: masks
  type: string
- container: ''
  name: mode
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: options
  type: reference
- container: ''
  name: output
  type: reference
- container: set
  name: outputs
  type: string
- container: ''
  name: overwrite
  type: boolean
- container: ''
  name: requiredPermissions
  type: reference
- container: ''
  name: storage
  type: string
- container: ''
  name: trim
  type: boolean
- container: ''
  name: type
  type: string
- container: ''
  name: version
  type: string
- container: ''
  name: width
  type: integer
property_count: 28
provider_name: Adobe Photoshop
provider_slug: adobe-photoshop
slug: adobe-photoshop-context
tags:
- AI/ML
- Creative Cloud
- Image Editing
- Photoshop
- Plugins
- REST API
- Scripting
- JSON-LD
- Linked Data
- Semantic Web
---
