---
class_count: 15
classes:
- APIRequest
- Field
- File
- FullItem
- GeneratorRecipe
- Item
- SectionRef
- Section
- ServerHealth
- Url
- VaultRef
- Vault
- description
- name
- version
context_file: json-ld/1password-connect-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/1password/refs/heads/main/json-ld/1password-connect-context.jsonld
description: JSON-LD context defining the semantic vocabulary for 1Password Connect from 1Password.
layout: jsonld
name: 1Password Connect Context
namespaces:
- prefix: onepassword
  uri: https://1password.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: account
  type: string
- container: ''
  name: action
  type: string
- container: ''
  name: actor
  type: reference
- container: ''
  name: attributeVersion
  type: integer
- container: ''
  name: category
  type: string
- container: set
  name: characterSets
  type: string
- container: ''
  name: content
  type: string
- container: ''
  name: contentVersion
  type: integer
- container: ''
  name: contentPath
  type: string
- container: ''
  name: createdAt
  type: dateTime
- container: set
  name: dependencies
  type: reference
- container: ''
  name: entropy
  type: decimal
- container: ''
  name: excludeCharacters
  type: string
- container: ''
  name: favorite
  type: boolean
- container: ''
  name: generate
  type: boolean
- container: ''
  name: href
  type: reference
- container: ''
  name: id
  type: string
- container: ''
  name: item
  type: reference
- container: ''
  name: itemVersion
  type: integer
- container: ''
  name: items
  type: integer
- container: ''
  name: jti
  type: string
- container: ''
  name: label
  type: string
- container: ''
  name: lastEditedBy
  type: string
- container: ''
  name: length
  type: integer
- container: ''
  name: message
  type: string
- container: ''
  name: primary
  type: boolean
- container: ''
  name: purpose
  type: string
- container: ''
  name: recipe
  type: string
- container: ''
  name: requestId
  type: string
- container: ''
  name: requestIp
  type: string
- container: ''
  name: resource
  type: reference
- container: ''
  name: result
  type: string
- container: ''
  name: section
  type: string
- container: ''
  name: service
  type: string
- container: ''
  name: size
  type: integer
- container: ''
  name: state
  type: string
- container: ''
  name: status
  type: string
- container: set
  name: tags
  type: string
- container: ''
  name: timestamp
  type: dateTime
- container: ''
  name: title
  type: string
- container: ''
  name: type
  type: string
- container: ''
  name: updatedAt
  type: dateTime
- container: set
  name: urls
  type: string
- container: ''
  name: userAgent
  type: string
- container: ''
  name: value
  type: string
- container: ''
  name: vault
  type: string
property_count: 46
provider_name: 1Password
provider_slug: 1password
slug: 1password-connect-context
tags:
- Password Manager
- Passwords
- Security
- Secrets
- JSON-LD
- Linked Data
- Semantic Web
---
