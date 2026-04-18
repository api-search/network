---
class_count: 33
classes:
- AudioObject
- ContactObject
- ConversationAnalytics
- CreateFlowRequest
- CreateTemplateRequest
- CursorPaging
- DocumentObject
- Flow
- FlowValidationError
- InteractiveMessage
- ListSection
- LocationMessage
- MediaObject
- MessageTemplate
- PhoneNumber
- ReactionMessage
- SendMessageRequest
- SendMessageResponse
- StickerObject
- SuccessResponse
- TemplateAnalytics
- TemplateButton
- TemplateComponent
- TemplateComponentDefinition
- TemplateMessage
- TemplateParameter
- TextMessage
- UpdateFlowRequest
- WhatsApp Flow JSON
- WhatsApp Message
- WhatsApp Message Template
- WhatsApp Webhook Payload
- WhatsAppBusinessAccount
context_file: json-ld/whatsapp-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/whatsapp/refs/heads/main/json-ld/whatsapp-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Whatsapp from WhatsApp.
layout: jsonld
name: Whatsapp Context
namespaces:
- prefix: wa
  uri: https://developers.facebook.com/docs/whatsapp/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: account_mode
  type: string
- container: ''
  name: action
  type: reference
- container: ''
  name: add_security_recommendation
  type: boolean
- container: ''
  name: address
  type: string
- container: set
  name: addresses
  type: string
- container: ''
  name: application_id
  type: string
- container: ''
  name: audio
  type: string
- container: ''
  name: birthday
  type: string
- container: ''
  name: biz_opaque_callback_data
  type: string
- container: ''
  name: body
  type: reference
- container: ''
  name: business_verification_status
  type: string
- container: set
  name: buttons
  type: string
- container: ''
  name: caption
  type: string
- container: set
  name: categories
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: clone_flow_id
  type: string
- container: ''
  name: code_expiration_minutes
  type: integer
- container: ''
  name: code_verification_status
  type: string
- container: ''
  name: column_end
  type: integer
- container: ''
  name: column_start
  type: integer
- container: set
  name: components
  type: string
- container: set
  name: contacts
  type: string
- container: ''
  name: context
  type: reference
- container: ''
  name: conversation_analytics
  type: reference
- container: ''
  name: country
  type: string
- container: ''
  name: coupon_code
  type: string
- container: ''
  name: currency
  type: string
- container: ''
  name: cursors
  type: reference
- container: ''
  name: data_api_version
  type: string
- container: ''
  name: date_time
  type: reference
- container: ''
  name: display_phone_number
  type: string
- container: ''
  name: document
  type: string
- container: set
  name: emails
  type: string
- container: ''
  name: emoji
  type: string
- container: ''
  name: endpoint_uri
  type: string
- container: set
  name: entry
  type: string
- container: ''
  name: error
  type: string
- container: ''
  name: error_type
  type: string
- container: ''
  name: example
  type: string
- container: ''
  name: filename
  type: string
- container: ''
  name: flow_action
  type: string
- container: ''
  name: flow_id
  type: string
- container: ''
  name: footer
  type: reference
- container: ''
  name: format
  type: string
- container: ''
  name: header
  type: reference
- container: ''
  name: id
  type: string
- container: ''
  name: image
  type: string
- container: ''
  name: index
  type: string
- container: ''
  name: interactive
  type: string
- container: ''
  name: is_official_business_account
  type: boolean
- container: ''
  name: json_version
  type: string
- container: ''
  name: language
  type: string
- container: ''
  name: latitude
  type: decimal
- container: ''
  name: line_end
  type: integer
- container: ''
  name: line_start
  type: integer
- container: ''
  name: link
  type: string
- container: ''
  name: location
  type: string
- container: ''
  name: longitude
  type: decimal
- container: ''
  name: message
  type: string
- container: ''
  name: message_id
  type: string
- container: ''
  name: message_template_namespace
  type: string
- container: set
  name: messages
  type: string
- container: ''
  name: messaging_limit_tier
  type: string
- container: ''
  name: messaging_product
  type: string
- container: ''
  name: name
  type: string
- container: ''
  name: name_status
  type: string
- container: ''
  name: navigate_screen
  type: string
- container: ''
  name: next
  type: string
- container: ''
  name: object
  type: string
- container: ''
  name: org
  type: reference
- container: ''
  name: owner_business
  type: reference
- container: ''
  name: parameter_format
  type: string
- container: set
  name: parameters
  type: string
- container: ''
  name: payload
  type: string
- container: ''
  name: phone_number
  type: string
- container: set
  name: phones
  type: string
- container: ''
  name: platform_type
  type: string
- container: set
  name: pointers
  type: string
- container: ''
  name: preview
  type: reference
- container: ''
  name: preview_url
  type: boolean
- container: ''
  name: previous
  type: string
- container: ''
  name: primary_funding_id
  type: string
- container: ''
  name: purchase_order_number
  type: string
- container: ''
  name: quality_rating
  type: string
- container: ''
  name: quality_score
  type: reference
- container: ''
  name: reaction
  type: string
- container: ''
  name: recipient_type
  type: string
- container: ''
  name: routing_model
  type: reference
- container: set
  name: rows
  type: string
- container: set
  name: screens
  type: string
- container: ''
  name: status
  type: string
- container: ''
  name: sticker
  type: string
- container: ''
  name: sub_type
  type: string
- container: ''
  name: success
  type: boolean
- container: ''
  name: template
  type: string
- container: ''
  name: template_analytics
  type: reference
- container: ''
  name: text
  type: string
- container: ''
  name: throughput
  type: reference
- container: ''
  name: timezone_id
  type: string
- container: ''
  name: title
  type: string
- container: ''
  name: to
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: url
  type: string
- container: set
  name: urls
  type: string
- container: set
  name: validation_errors
  type: string
- container: ''
  name: verified_name
  type: string
- container: ''
  name: version
  type: string
- container: ''
  name: video
  type: string
- container: ''
  name: whatsapp_business_account
  type: reference
property_count: 109
provider_name: WhatsApp
provider_slug: whatsapp
slug: whatsapp-context
tags:
- JSON-LD
- Linked Data
- Semantic Web
---
