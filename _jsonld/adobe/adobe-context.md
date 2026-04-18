---
class_count: 45
classes:
- id
- type
- PDFJob
- Asset
- InputAsset
- OutputAsset
- PageRange
- PDFProperties
- PageProperties
- PasswordProtection
- Permissions
- ExtractOptions
- JobError
- CreatePDFOperation
- ExportPDFOperation
- CombinePDFOperation
- SplitPDFOperation
- OCROperation
- CompressPDFOperation
- ProtectPDFOperation
- RemoveProtectionOperation
- LinearizePDFOperation
- ExtractPDFOperation
- AutoTagOperation
- DocumentGenerationOperation
- status
- error
- metadata
- userPassword
- ownerPassword
- password
- permissions
- jsonDataForMerge
- fragments
- title
- description
- author
- creator
- producer
- code
- message
- passwordProtection
- splitOptions
- basePagesRange
- assetPagesRange
context_file: json-ld/adobe-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/json-ld/adobe-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Adobe from Adobe.
layout: jsonld
name: Adobe Context
namespaces:
- prefix: adobe
  uri: https://ns.adobe.com/pdf-services/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: schema
  uri: https://schema.org/
properties:
- container: ''
  name: assetID
  type: string
- container: ''
  name: uploadUri
  type: reference
- container: ''
  name: downloadUri
  type: reference
- container: ''
  name: asset
  type: reference
- container: ''
  name: mediaType
  type: string
- container: ''
  name: size
  type: integer
- container: ''
  name: start
  type: integer
- container: ''
  name: end
  type: integer
- container: list
  name: pageRanges
  type: ''
- container: list
  name: pagesOrder
  type: ''
- container: list
  name: pageActions
  type: ''
- container: ''
  name: rotation
  type: integer
- container: list
  name: assets
  type: ''
- container: list
  name: assetsToInsert
  type: ''
- container: list
  name: assetsToReplace
  type: ''
- container: ''
  name: baseAssetID
  type: string
- container: ''
  name: insertAt
  type: integer
- container: ''
  name: targetFormat
  type: string
- container: ''
  name: documentLanguage
  type: string
- container: ''
  name: ocrLanguage
  type: string
- container: ''
  name: ocrType
  type: string
- container: ''
  name: compressionLevel
  type: string
- container: ''
  name: outputFormat
  type: string
- container: ''
  name: encryptionAlgorithm
  type: string
- container: ''
  name: printQuality
  type: string
- container: ''
  name: editContent
  type: boolean
- container: ''
  name: copyContent
  type: boolean
- container: ''
  name: editAnnotations
  type: boolean
- container: ''
  name: fillForms
  type: boolean
- container: ''
  name: assembleDocument
  type: boolean
- container: list
  name: elementsToExtract
  type: ''
- container: list
  name: elementsToExtractRenditions
  type: ''
- container: ''
  name: tableOutputFormat
  type: string
- container: ''
  name: getStylingInfo
  type: boolean
- container: ''
  name: addCharInfo
  type: boolean
- container: ''
  name: generateReport
  type: boolean
- container: ''
  name: shiftHeadings
  type: boolean
- container: ''
  name: includePageLevelProperties
  type: boolean
- container: ''
  name: pageCount
  type: integer
- container: ''
  name: pdfVersion
  type: string
- container: ''
  name: isEncrypted
  type: boolean
- container: ''
  name: isLinearized
  type: boolean
- container: ''
  name: hasFormFields
  type: boolean
- container: ''
  name: isTagged
  type: boolean
- container: ''
  name: pageNumber
  type: integer
- container: ''
  name: width
  type: decimal
- container: ''
  name: height
  type: decimal
- container: list
  name: pages
  type: ''
- container: ''
  name: createdDate
  type: dateTime
- container: ''
  name: modifiedDate
  type: dateTime
- container: ''
  name: fileCount
  type: integer
property_count: 51
provider_name: Adobe
provider_slug: adobe
slug: adobe-context
tags:
- Analytics
- Creative Cloud
- Digital Asset Management
- Document Services
- E-Commerce
- E-Signatures
- Experience Cloud
- Generative AI
- Marketing
- PDF
- Work Management
- JSON-LD
- Linked Data
- Semantic Web
---
