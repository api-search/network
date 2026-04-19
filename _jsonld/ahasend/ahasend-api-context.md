---
class_count: 9
classes:
- email
- name
- Contact
- Attachment
- Content
- Email
- SuccessfulResponse
- BadRequestResponse
- AccessDeniedResponse
context_file: json-ld/ahasend-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/ahasend/refs/heads/main/json-ld/ahasend-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Ahasend Api from AhaSend.
layout: jsonld
name: Ahasend Api Context
namespaces:
- prefix: ahasend
  uri: https://ahasend.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: data
  type: string
- container: ''
  name: base64
  type: boolean
- container: ''
  name: contentType
  type: string
- container: ''
  name: contentId
  type: string
- container: ''
  name: fileName
  type: string
- container: ''
  name: subject
  type: string
- container: ''
  name: textBody
  type: string
- container: ''
  name: htmlBody
  type: string
- container: set
  name: attachments
  type: string
- container: ''
  name: replyTo
  type: string
- container: ''
  name: headers
  type: reference
- container: ''
  name: from
  type: string
- container: set
  name: recipients
  type: string
- container: ''
  name: content
  type: string
- container: ''
  name: successCount
  type: integer
- container: ''
  name: failCount
  type: integer
- container: set
  name: failedRecipients
  type: string
- container: set
  name: errors
  type: string
- container: ''
  name: status
  type: string
property_count: 19
provider_name: AhaSend
provider_slug: ahasend
slug: ahasend-api-context
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
- JSON-LD
- Linked Data
- Semantic Web
---
