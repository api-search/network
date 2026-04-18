---
class_count: 22
classes:
- CallbackCompletionRequest
- BatchCallbackCompletionRequest
- BatchCallbackInput
- BatchCallbackResponse
- BatchCallbackError
- ActionDefinition
- ActionDefinitionInput
- ActionDefinitionPatch
- ActionLabels
- InputField
- OutputField
- FieldTypeDefinition
- FieldOption
- ObjectRequestOptions
- ActionFunctionReference
- ActionDefinitionCollection
- ActionFunction
- ActionFunctionInput
- ActionFunctionCollection
- ActionDefinitionRevision
- ActionDefinitionRevisionCollection
- Paging
context_file: json-ld/hubspot-custom-workflow-actions-api-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/hubspot/refs/heads/main/json-ld/hubspot-custom-workflow-actions-api-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Hubspot Custom Workflow Actions Api from HubSpot.
layout: jsonld
name: Hubspot Custom Workflow Actions Api Context
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
  name: outputFields
  type: reference
- container: set
  name: inputs
  type: reference
- container: ''
  name: callbackId
  type: string
- container: ''
  name: status
  type: string
- container: set
  name: errors
  type: reference
- container: ''
  name: message
  type: string
- container: ''
  name: category
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: revisionId
  type: string
- container: ''
  name: actionUrl
  type: reference
- container: ''
  name: labels
  type: reference
- container: set
  name: inputFields
  type: reference
- container: set
  name: objectTypes
  type: string
- container: ''
  name: objectRequestOptions
  type: reference
- container: ''
  name: published
  type: boolean
- container: set
  name: functions
  type: reference
- container: ''
  name: actionName
  type: string
- container: ''
  name: actionDescription
  type: string
- container: ''
  name: appDisplayName
  type: string
- container: ''
  name: actionCardContent
  type: string
- container: ''
  name: typeDefinition
  type: reference
- container: set
  name: supportedValueTypes
  type: string
- container: ''
  name: isRequired
  type: boolean
- container: ''
  name: name
  type: ''
- container: ''
  name: type
  type: string
- container: ''
  name: fieldType
  type: string
- container: ''
  name: label
  type: string
- container: ''
  name: description
  type: ''
- container: set
  name: options
  type: reference
- container: ''
  name: value
  type: string
- container: ''
  name: displayOrder
  type: integer
- container: set
  name: properties
  type: string
- container: ''
  name: functionType
  type: string
- container: set
  name: results
  type: reference
- container: ''
  name: paging
  type: reference
- container: ''
  name: functionSource
  type: string
- container: ''
  name: definition
  type: reference
- container: ''
  name: createdAt
  type: dateTime
- container: ''
  name: next
  type: reference
property_count: 39
provider_name: HubSpot
provider_slug: hubspot
slug: hubspot-custom-workflow-actions-api-context
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
