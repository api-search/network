---
class_count: 56
classes:
- Adobe Creative Suite Image Job
- Adobe Firefly Generation Request and Response
- Adobe Stock File
- Asset
- AssetReference
- AssetUploadRequest
- AssetUploadResponse
- AsyncJobSubmitted
- AutoTagRequest
- Category
- CombinePDFRequest
- CompressPDFRequest
- CreatePDFRequest
- CutoutRequest
- DocumentGenerationRequest
- DocumentOperations
- DocumentOperationsRequest
- ErrorResponse
- ExportPDFRequest
- GenerateSimilarRequest
- GenerationStatus
- ImageExpandRequest
- ImageFillRequest
- ImageGenerateRequest
- ImageSize
- InputImageReference
- JobInput
- JobOutput
- JobStatus
- JobSubmitted
- Layer
- LayerManageRequest
- LicenseHistoryResult
- LicenseReference
- LicenseRequest
- LicenseResponse
- LicenseStatsResponse
- LinearizePDFRequest
- MaskRequest
- MemberProfile
- OCRRequest
- ObjectCompositeRequest
- OperationStatus
- OperationSubmitted
- OutputImage
- PageRange
- ProductCropRequest
- RenderOutput
- RenditionCreateRequest
- SearchResult
- StockFile
- StockFileResponse
- StraightenRequest
- StyleOptions
- TextEditRequest
- VideoGenerateRequest
context_file: json-ld/adobe-creative-suite-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adobe-creative-suite/refs/heads/main/json-ld/adobe-creative-suite-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adobe Creative Suite from Adobe Creative Suite.
layout: jsonld
name: Adobe Creative Suite Context
namespaces:
- prefix: adobe
  uri: https://developer.adobe.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: _links
  type: reference
- container: ''
  name: asset
  type: string
- container: ''
  name: assetID
  type: string
- container: set
  name: assets
  type: string
- container: ''
  name: blendMode
  type: string
- container: ''
  name: bounds
  type: reference
- container: ''
  name: category
  type: reference
- container: set
  name: children
  type: string
- container: ''
  name: code
  type: string
- container: ''
  name: comp_url
  type: string
- container: ''
  name: compressionLevel
  type: string
- container: ''
  name: contentClass
  type: string
- container: ''
  name: content_id
  type: integer
- container: ''
  name: content_type
  type: string
- container: ''
  name: country_name
  type: string
- container: ''
  name: created
  type: dateTime
- container: ''
  name: creator_id
  type: integer
- container: ''
  name: creator_name
  type: string
- container: ''
  name: details
  type: string
- container: ''
  name: documentLanguage
  type: string
- container: ''
  name: downloadUri
  type: string
- container: ''
  name: download_url
  type: string
- container: ''
  name: duration
  type: decimal
- container: ''
  name: end
  type: integer
- container: set
  name: errors
  type: string
- container: ''
  name: exportOCRLocale
  type: string
- container: set
  name: files
  type: string
- container: ''
  name: flatten
  type: boolean
- container: ''
  name: generateReport
  type: boolean
- container: ''
  name: has_releases
  type: boolean
- container: ''
  name: height
  type: integer
- container: ''
  name: href
  type: string
- container: ''
  name: id
  type: integer
- container: ''
  name: image
  type: string
- container: ''
  name: index
  type: integer
- container: ''
  name: input
  type: reference
- container: set
  name: inputs
  type: string
- container: ''
  name: is_editorial
  type: boolean
- container: ''
  name: is_licensed
  type: string
- container: ''
  name: jobID
  type: string
- container: ''
  name: jobId
  type: string
- container: ''
  name: jsonDataForMerge
  type: reference
- container: set
  name: keywords
  type: string
- container: ''
  name: license
  type: string
- container: ''
  name: link
  type: string
- container: ''
  name: locale
  type: string
- container: ''
  name: locked
  type: boolean
- container: ''
  name: mask
  type: string
- container: ''
  name: mediaType
  type: string
- container: ''
  name: media_type_id
  type: integer
- container: ''
  name: message
  type: string
- container: ''
  name: modified
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
  name: notTaggedAdds
  type: boolean
- container: ''
  name: numVariations
  type: integer
- container: ''
  name: ocrLang
  type: string
- container: ''
  name: opacity
  type: integer
- container: ''
  name: options
  type: string
- container: ''
  name: output
  type: reference
- container: ''
  name: outputFormat
  type: string
- container: set
  name: outputs
  type: string
- container: ''
  name: overwrite
  type: boolean
- container: ''
  name: placement
  type: reference
- container: ''
  name: premium_level_id
  type: integer
- container: set
  name: presets
  type: string
- container: ''
  name: prompt
  type: string
- container: ''
  name: purchase_details
  type: reference
- container: ''
  name: purchase_params
  type: reference
- container: ''
  name: referenceImage
  type: string
- container: ''
  name: requestId
  type: string
- container: ''
  name: resize
  type: reference
- container: ''
  name: seed
  type: integer
- container: set
  name: seeds
  type: string
- container: ''
  name: shiftHeadings
  type: boolean
- container: ''
  name: size
  type: string
- container: ''
  name: source
  type: reference
- container: ''
  name: start
  type: integer
- container: ''
  name: status
  type: string
- container: ''
  name: statusUrl
  type: string
- container: ''
  name: stock_user
  type: reference
- container: ''
  name: storage
  type: string
- container: ''
  name: strength
  type: integer
- container: ''
  name: style
  type: string
- container: ''
  name: targetFormat
  type: string
- container: ''
  name: thumbnail_1000_url
  type: string
- container: ''
  name: thumbnail_500_url
  type: string
- container: ''
  name: thumbnail_height
  type: integer
- container: ''
  name: thumbnail_url
  type: string
- container: ''
  name: thumbnail_width
  type: integer
- container: ''
  name: title
  type: string
- container: ''
  name: trim
  type: reference
- container: ''
  name: type
  type: string
- container: ''
  name: uploadUri
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: vector_type
  type: string
- container: ''
  name: visible
  type: boolean
- container: ''
  name: width
  type: integer
property_count: 99
provider_name: Adobe Creative Suite
provider_slug: adobe-creative-suite
slug: adobe-creative-suite-context
tags:
- Creative
- Design
- Graphics
- Photography
- Video
- JSON-LD
- Linked Data
- Semantic Web
---
